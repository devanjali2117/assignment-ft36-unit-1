import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Sample Input
point1 = (2, 3)
point2 = (5, 7)

# Function Call and Output
distance_result = distance(point1[0], point1[1], point2[0], point2[1])
print(f"distance = {distance_result}")
