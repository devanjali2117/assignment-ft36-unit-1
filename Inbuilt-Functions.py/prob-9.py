def find(s, substring):
    len_sub = len(substring)
    len_s = len(s)

    for i in range(len_s - len_sub):
        if s[i:i+len_sub] == substring:
            return i
    return -1

s = 'Look for the substring in this string.'
substring = 'substring'
output = find(s, substring)
print(output)