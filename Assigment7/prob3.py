def print_brick_wall(height, width):
    for i in range(height):
        if i % 2 == 0:
            print("[]" * width)
        else:
            print(" " + "[]" * (width - 1))

# Reading input
H = int(input("Enter height: "))
W = int(input("Enter width: "))

# Printing brick wall
print_brick_wall(H, W)