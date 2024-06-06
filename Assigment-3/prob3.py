# Decimal to Binary
decimal_number_1 = 54
decimal_number_2 = 120

binary_number_1 = bin(decimal_number_1)[2:]
binary_number_2 = bin(decimal_number_2)[2:]

print(f"(54)10 = {binary_number_1}2")
print(f"(120)10 = {binary_number_2}2")

# Decimal to Octal
decimal_number_3 = 76
decimal_number_4 = 889

octal_number_1 = oct(decimal_number_3)[2:]
octal_number_2 = oct(decimal_number_4)[2:]

print(f"(76)10 = {octal_number_1}8")
print(f"(889)10 = {octal_number_2}8")

# Decimal to Hexadecimal
decimal_number_5 = 789
decimal_number_6 = 108

hexadecimal_number_1 = hex(decimal_number_5)[2:].upper()
hexadecimal_number_2 = hex(decimal_number_6)[2:].upper()

print(f"(789)10 = {hexadecimal_number_1}16")
print(f"(108)10 = {hexadecimal_number_2}16")
