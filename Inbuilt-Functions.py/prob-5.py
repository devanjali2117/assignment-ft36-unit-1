def contains(my_list, value):
    for item in my_list:
        if item == value:
            return True
    return False

my_list = [1, 2, 3, 4, 5]
value = 3

contains_value = contains(my_list, value)

print(contains_value)