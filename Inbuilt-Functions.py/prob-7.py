def count(lst, value):
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count

lst = [1, 2, 2, 3, 4, 2]
value_to_count = 2
output = count(lst, value_to_count)
print(output)

s = 'hello world'
char_to_count = 'o'
output = count(s, char_to_count)
print(output)