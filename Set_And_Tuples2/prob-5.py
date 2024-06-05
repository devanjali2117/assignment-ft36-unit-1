# Problem 5: Maximum and Minimum in a Tuple
# Description: Write a Python program to find the maximum and minimum numbers in a tuple of integers without using the built-in max() and min() functions.
# Sample Input: (5, 10, 3, 15, 2, 20)
# Sample Output:
# Maximum: 20
# Minimum: 2


input_tuple = (5, 10, 3, 15, 2, 20)

max_num = input_tuple[0]
min_num = input_tuple[0]

for num in input_tuple:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum :", max_num)
print("Minimum :", min_num)