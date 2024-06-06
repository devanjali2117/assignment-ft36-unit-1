# Function to convert binary to octal
def binary_to_octal(binary_number):
    decimal_number = int(binary_number, 2)
    return oct(decimal_number)[2:]

# Function to convert binary to hexadecimal
def binary_to_hexadecimal(binary_number):
    decimal_number = int(binary_number, 2)
    return hex(decimal_number)[2:].upper()

# Given Binary Numbers
binary_numbers = ["1110001000", "110110101", "1010100"]

# Conversion and Printing Results
for binary in binary_numbers:
    octal = binary_to_octal(binary)
    hexadecimal = binary_to_hexadecimal(binary)
    print(f"({binary})2 = ({octal})8 = ({hexadecimal})16")
