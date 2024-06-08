def rindex(my_list, value):
  last_index = -1
  for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == value:
      last_index = i
      break

  return last_index

my_list = [1, 2, 3, 2, 4]
value = 2

last_index = rindex(my_list, value)

print(last_index)