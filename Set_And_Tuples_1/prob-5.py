### Problem 5: Find the Largest Number in a List

# **Description:** Write a Python program to find the largest number in a given list.

# **Sample Input:** `[4, 65, 32, 2, 104, 78, 10]`

# **Sample Output:** `104`
# Given list of numbers
numbers = [4, 65, 32, 2, 104, 78, 10]

# Initialize a variable to store the largest number
largest_number = numbers[0]

# Iterate over the list to find the largest number
for num in numbers:
    if num > largest_number:
        largest_number = num

# Print the largest number
print("The largest number in the list is:", largest_number)