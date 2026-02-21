user_answer = input(f'What is the Answer to the Great Question of Life, the Universe, and Everything? ').strip().lower().replace('-', ' ')
print('Yes') if user_answer == "forty two" or user_answer == '42' else print('No')
