# Decimal to Binary, Octal, and Hexadecimal
decimal_number = 42

binary_number = bin(decimal_number)
octal_number = oct(decimal_number)
hexadecimal_number = hex(decimal_number)

print(f"Decimal {decimal_number} in binary is {binary_number}")
print(f"Decimal {decimal_number} in octal is {octal_number}")
print(f"Decimal {decimal_number} in hexadecimal is {hexadecimal_number}")

# Binary, Octal, and Hexadecimal to Decimal
binary_number = "101010"
octal_number = "52"
hexadecimal_number = "2a"

decimal_from_binary = int(binary_number, 2)
decimal_from_octal = int(octal_number, 8)
decimal_from_hexadecimal = int(hexadecimal_number, 16)

print(f"Binary {binary_number} in decimal is {decimal_from_binary}")
print(f"Octal {octal_number} in decimal is {decimal_from_octal}")
print(f"Hexadecimal {hexadecimal_number} in decimal is {decimal_from_hexadecimal}")
