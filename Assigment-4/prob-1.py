def calculate_triangle_area(base, height):
    # Check if either base or height is zero, then return 0.0
    if base == 0 or height == 0:
        return 0.0
    # Check if either base or height is negative, then print error message
    elif base < 0 or height < 0:
        print("Invalid input, base and height must be positive numbers.")
        return None
    else:
        # Calculate the area using the formula and return the result
        area = (base * height) / 2
        return area

    # Prompt the user to input the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

    # Calculate the area of the triangle
area = calculate_triangle_area(base, height)

if area is not None:
        # Print the result in a formatted string
    print(f"The area of the triangle is: {area}")