price_bottle, amount_due, insert_coin, change_owed, total_counter = 50, 0, 0, 0, 0
accepted_coins = [5, 10, 25]
while total_counter < price_bottle:
    insert_coin = int(input('Insert Coin: '))
    if insert_coin in accepted_coins:
        total_counter += insert_coin
        insert_coin = 0
        amount_due = price_bottle - total_counter
        change_owed = total_counter - price_bottle
        if change_owed < 0:
            print(f'Amount Due: {amount_due}')
        else:
            print(f'Change Owed: {change_owed}')
    else:
        amount_due = price_bottle - total_counter
        change_owed = total_counter - price_bottle
        insert_coin = 0
        if change_owed < 0:
            print(f'Amount Due: {amount_due}')
        else:
            print(f'Change Owed: {change_owed}')
