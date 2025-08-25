from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='../static')

# DB Connection
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="bank_system"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name = request.form['name']
        balance = request.form['balance']
        cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, balance))
        db.commit()
        return redirect('/')
    return render_template('create_account.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        acc_id = request.form['id']
        amount = float(request.form['amount'])
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, acc_id))
        db.commit()
        return redirect('/')
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        acc_id = request.form['id']
        amount = float(request.form['amount'])
        cursor.execute("SELECT balance FROM accounts WHERE id = %s", (acc_id,))
        current = cursor.fetchone()
        if current and current[0] >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, acc_id))
            db.commit()
        return redirect('/')
    return render_template('withdraw.html')

@app.route('/accounts')1
def view_accounts():
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    return render_template('view_accounts.html', accounts=accounts)

if __name__ == '__main__':
    app.run(debug=True)

