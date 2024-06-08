def reverse(sequence):
    reversed_sequence = []
    for i in range(len(sequence) - 1, -1, -1):
        reversed_sequence.append(sequence[i])

    if isinstance(sequence, str):
        return ''.join(reversed_sequence)
    return reversed_sequence

lst = [1, 2, 3, 4, 5]
output_list = reverse(lst)
print(output_list)

s = 'hello'
output_string = reverse(s)
print(output_string)