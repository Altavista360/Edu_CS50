input_expression = input('Expression: ').strip()
input_x, y, input_z = input_expression.split(" ")
x = int(input_x)
z = int(input_z)
if y == '+':
    result = x ++ z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/' and z != 0:
    result = x / z
print(f'{result:.1f}')
