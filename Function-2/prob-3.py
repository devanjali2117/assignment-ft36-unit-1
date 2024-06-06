def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

# Given dimensions
length = 5
width = 3

# Calculate area and perimeter
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
