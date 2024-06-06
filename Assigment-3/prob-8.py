# Hexadecimal to Binary Conversion Function
def hexadecimal_to_binary(hexadecimal_str):
    binary_str = ""
    for digit in hexadecimal_str:
        binary_str += format(int(digit, 16), '04b')  # Converts each hexadecimal digit to 4-bit binary
    return binary_str

# Given Hexadecimal Numbers
hexadecimal_numbers = ["4026", "BCA1", "98E"]

# Conversion and Printing Results
binary_results = [hexadecimal_to_binary(num) for num in hexadecimal_numbers]

for hexadecimal, binary in zip(hexadecimal_numbers, binary_results):
    print(f"({hexadecimal})16 = ({binary})2")
