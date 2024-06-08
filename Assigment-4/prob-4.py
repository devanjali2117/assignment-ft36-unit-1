def calculate_simple_interest(principal, rate, time):
    # Check if any of the input values are negative
    if principal < 0 or rate < 0 or time < 0:
        print("Invalid input, all values must be non-negative.")
    else:
        # Calculate the simple interest using the formula
        simple_interest = (principal * rate * time) / 100
        return simple_interest
# Prompt the user to input the principal amount
principal = float(input("Enter the principal amount: "))
# Prompt the user to input the rate of interest per year
rate = float(input("Enter the rate of interest per year: "))
# Prompt the user to input the time in years
time = float(input("Enter the time in years: "))

# Calculate the simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

if simple_interest is not None:
     # Print the result in a formatted string
    print(f"The simple interest is: {simple_interest}")