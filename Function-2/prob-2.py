def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

# Sample dimensions
length = 5
width = 3

# Calculate area and perimeter
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

# Output the results
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")
