### Problem 6 : Set Difference for More Than Two Sets

# **Description:** Write a Python program to find the set difference (elements present in the first set but not in the others) for more than two sets without using the built-in difference method.

# **Sample Input:**

# - Set 1: `{10, 20, 30, 40, 50}`
# - Set 2: `{30, 40, 60, 70}`
# - Set 3: `{50, 60, 90}`

# **Sample Output:** `{10, 20}`
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}
set3 = {50, 60, 90}

difference_set = set()
for element in set1:
    if element not in set2 and element not in set3:
        difference_set.add(element)

print("Set of difference is:", difference_set)