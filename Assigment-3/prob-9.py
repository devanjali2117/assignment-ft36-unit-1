# ASCII Conversion Function
def text_to_ascii(text):
    ascii_codes = []
    for char in text:
        ascii_code = ord(char)
        ascii_codes.append(ascii_code)
    return ascii_codes

# Given Texts
texts = ["HOTS", "Main", "CaSe"]

# Conversion and Printing Results
for text in texts:
    ascii_codes = text_to_ascii(text)
    print(f"ASCII codes for '{text}': {ascii_codes}")
