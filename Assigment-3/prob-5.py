# Decimal to Hexadecimal Conversion Function
def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

# Given Decimal Numbers
decimal_numbers = [548, 4052, 58]

# Conversion and Printing Results
hexadecimal_results = [decimal_to_hexadecimal(num) for num in decimal_numbers]

for decimal, hexadecimal in zip(decimal_numbers, hexadecimal_results):
    print(f"({decimal})10 = ({hexadecimal})16")
