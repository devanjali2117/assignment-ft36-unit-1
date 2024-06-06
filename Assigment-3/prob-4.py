# Octal to Decimal Conversion Function
def octal_to_decimal(octal_number):
    return int(octal_number, 8)

# Given Octal Numbers
octal_numbers = ["145", "6760", "455"]

# Conversion and Printing Results
decimal_results = [octal_to_decimal(num) for num in octal_numbers]

for octal, decimal in zip(octal_numbers, decimal_results):
    print(f"({octal})8 = ({decimal})10")
