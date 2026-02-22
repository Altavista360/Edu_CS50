counter = 0

menu_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

while True:
    try:
        input_value = input('Item: ').lower().title()
        if input_value in menu_dict:
            counter += menu_dict.get(input_value)
            print(f'Total: ${counter:.2f}')

    except EOFError:
        print(f'Total: ${counter:.2f}')
        break

    except:
        pass
