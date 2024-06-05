### Problem 1: Set Union Without Duplicates

# **Description:** Write a Python program to perform the union of three sets without using the built-in union method. Ensure there are no duplicates in the final set.

# **Sample Input:**

# - Set 1: `{1, 2, 3}`
# - Set 2: `{3, 4, 5}`
# - Set 3: `{5, 6, 7}`

# **Sample Output:** `{1, 2, 3, 4, 5, 6, 7}`

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

result_set = set(set1)
result_set.update(set2)
result_set.update(set3)

print(result_set)