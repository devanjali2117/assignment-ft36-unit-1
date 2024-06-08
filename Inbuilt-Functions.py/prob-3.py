def slice(my_list, start, end):
    return my_list[start:end]

my_list = [1, 2, 3, 4, 5]
start = 1
end = 4

sliced_list = slice(my_list, start, end)

print(sliced_list)