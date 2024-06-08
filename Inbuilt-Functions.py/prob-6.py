def index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    raise ValueError(f"{value} is not in list")

lst = [1, 2, 3, 4, 5]
value_to_find = 3
output = index(lst, value_to_find)
print(output)