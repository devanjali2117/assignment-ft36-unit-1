def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Sample Input
x1, y1 = 2, 3
x2, y2 = 5, 7

# Sample Output
dist = distance(x1, y1, x2, y2)
print("Distance:", dist)