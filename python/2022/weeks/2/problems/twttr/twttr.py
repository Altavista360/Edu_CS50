input_string = input('Input: ')
ignore_letters = ['A', 'E', 'I', 'O', 'U']
print('Output: ', end='')
for i in input_string:
    if i.upper() in ignore_letters:
        continue
    else:
        print(i, end='')
