# **Description:** Write a Python program to find the difference between two sets. The difference is a set of elements that are in the first set but not in the second set.

# **Sample Input:**

# - Set 1: `{10, 20, 30, 40, 50}`
# - Set 2: `{40, 50, 60, 70, 80}`

# **Sample Output:** `{10, 20, 30}`

set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

difference = set1.difference(set2)

print(difference)