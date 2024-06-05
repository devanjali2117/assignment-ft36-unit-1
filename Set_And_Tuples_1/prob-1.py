### Problem 1: Unique Element Finder

# **Description:** Write a Python program to find all the unique elements in a given list. Your program should display the unique elements in the form of a list.

# **Sample Input:** `[1, 2, 2, 3, 4, 5, 3, 6, 4]`

# **Sample Output:** `[1, 5, 6]`

input_list = [1, 2, 2, 3, 4, 5, 3, 6, 4]

unique_elements = list(set(input_list))

print(unique_elements)