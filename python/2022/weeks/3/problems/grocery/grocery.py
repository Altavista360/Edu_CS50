grocery_dict = dict(list())

while True:
    try:
        input_string = input().strip().upper()
        if input_string not in grocery_dict:
            grocery_dict[input_string] = 1
        else:
            grocery_dict[input_string] += 1

    except EOFError:
        results = dict(sorted(list(grocery_dict.items())))
        for input_string in results:
            print(f'{results[input_string]} {input_string}')
        break

    except:
        pass
