### Problem 4: Subset Verification

# **Description:** Write a Python program to check if a set is a subset of another set. Do not use the built-in method for subset verification.

# **Sample Input:**

# - Set 1 (potential subset): `{1, 2, 3}`
# - Set 2: `{1, 2, 3, 4, 5, 6}`

# **Sample Output:** `True`

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}

is_subset = all(elem in set2 for elem in set1)

if is_subset:
    print("True")
else:
    print("False")