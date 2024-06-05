### Problem 2: Tuple Sum

# **Description:** Write a Python program to calculate the sum of all numbers in a given tuple.

# **Sample Input:** `(8, 2, 3, 0, 7)`

# **Sample Output:** `20`
def sumoftuple(tup):

	# Converting into list
	test = list(tup)

	# Initializing count
	count = 0

	# body of function starts here
	for i in test:
		count += i
	return count
    # body of function ends here

# Initializing test_tup
tup = (8,2,3,0,7)
print(sum(tup))