# Get temperature input from the user
temperature = float(input("Enter the temperature in Celsius: "))

# Check the temperature condition
if temperature < 15:
    print("It's Cold.")
elif temperature <= 25:
    print("It's Warm.")
else:
    print("It's Hot.")
