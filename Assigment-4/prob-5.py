def calculate_bmi(weight, height):
    # Check for invalid inputs
    if height == 0:
        print("Invalid input, height cannot be zero.")
    elif weight < 0 or height < 0:
        print("Invalid input, height and weight must be positive numbers.")
    else:
        # Calculate the BMI using the formula
        bmi = weight / (height * height)

# Prompt the user to input their weight in kilograms
weight = float(input("Enter your weight in kilograms: "))
# Prompt the user to input their height in meters
height = float(input("Enter your height in meters: "))

# Calculate the BMI
bmi = calculate_bmi(weight, height)

if bmi is not None:
    # Print the BMI, rounded to two decimal places
    print(f"Your BMI is: {bmi}")