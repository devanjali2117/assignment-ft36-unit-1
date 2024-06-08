def compare_numbers(num1, num2):
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num1 < num2:
        return f"{num2} is larger than {num1}"
    else:
        return "Both numbers are equal"
# Prompt the user to input the first number        
num1 = float(input("Enter the first number: "))
    # Prompt the user to input the second number
num2 = float(input("Enter the second number: "))

    # Compare the numbers and get the result
result = compare_numbers(num1, num2)

    # Print the result in a formatted string
print(result)        