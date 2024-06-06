# Decimal to Octal
decimal_number = 514
octal_number = oct(decimal_number)
print(f"(514)10 = {octal_number[2:]}8")

# Octal to Decimal
octal_number = "220"
decimal_from_octal = int(octal_number, 8)
print(f"(220)8 = {decimal_from_octal}10")

# Hexadecimal to Decimal
hex_number_1 = "76F"
hex_number_2 = "4D9"

decimal_from_hex_1 = int(hex_number_1, 16)
decimal_from_hex_2 = int(hex_number_2, 16)

print(f"(76F)16 = {decimal_from_hex_1}10")
print(f"(4D9)16 = {decimal_from_hex_2}10")

# Binary to Decimal
binary_number_1 = "11001010"
binary_number_2 = "1010111"

decimal_from_binary_1 = int(binary_number_1, 2)
decimal_from_binary_2 = int(binary_number_2, 2)

print(f"(11001010)2 = {decimal_from_binary_1}10")
print(f"(1010111)2 = {decimal_from_binary_2}10")
