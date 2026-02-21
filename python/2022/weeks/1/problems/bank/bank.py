current_greetings = input(f'Greeting: ').strip().lower()
if current_greetings.startswith('hello'):
    print('$0')
elif current_greetings[0] == 'h':
    print('$20')
else:
    print('$100')
