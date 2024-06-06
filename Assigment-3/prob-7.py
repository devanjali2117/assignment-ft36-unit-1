# Octal to Binary Conversion Function
def octal_to_binary(octal_str):
    binary_str = ""
    for digit in octal_str:
        binary_str += format(int(digit, 8), '03b')  # Converts each octal digit to 3-bit binary
    return binary_str

# Given Octal Numbers
octal_numbers = ["2306", "5610", "742"]

# Conversion and Printing Results
binary_results = [octal_to_binary(num) for num in octal_numbers]

for octal, binary in zip(octal_numbers, binary_results):
    print(f"({octal})8 = ({binary})2")
