### Problem 7: Remove Duplicates

# **Description:** Given a list of numbers, write a Python program to remove all duplicates and return a tuple with the remaining elements sorted in ascending order.

# **Sample Input:** `[1, 2, 3, 4, 3, 2, 1]`

# **Sample Output:** `(1, 2, 3, 4)`
def remove_duplicates_and_sort(sample_list):
    unique_elements = list(set(sample_list))
    unique_elements.sort()
    return tuple(unique_elements)

sample_list = [1, 2, 3, 4, 3, 2, 1]
result = remove_duplicates_and_sort(sample_list)
print(result)