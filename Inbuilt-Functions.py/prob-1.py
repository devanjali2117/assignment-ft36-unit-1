def join(string_list, separator):
    result = ""
    for i in range(len(string_list)):
        result += string_list[i]
        if i < len(string_list) - 1:
            result += separator
    return result

strings = ['Hello', 'World']
separator = ' '
output = join(strings, separator)
print(output)