### Problem 3: Set Operations - Union and Intersection

# **Description:** Given two sets, write a Python program to perform the following operations:

# - Print their union.
# - Print their intersection.

# **Sample Input:**

# - Set 1: `{1, 2, 3, 4, 5}`
# - Set 2: `{4, 5, 6, 7, 8}`

# **Sample Output:**

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Initialize empty sets for union and intersection
union_set = set()
intersection_set = set()

# Calculate Union using loop
for element in set1:
    union_set.add(element)

for element in set2:
    union_set.add(element)

# Calculate Intersection using loop
for element in set1:
    if element in set2:
        intersection_set.add(element)

# Print the union and intersection
print("Union of the two sets:", union_set)
print("Intersection of the two sets:", intersection_set)