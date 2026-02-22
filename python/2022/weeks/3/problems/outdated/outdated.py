months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    input_value = input('Date: ').strip().lower().title()
    try:
        month, day, year = input_value.split('/')
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31) and (len(year) == 4):
            month = int(month)
            day = int(day)
            year = int(year)
            print(f'{year}-{month:02}-{day:02}')
            break

    except ValueError:
        try:
            month, day, year = input_value.split(' ')
            day = day[:-1]
            if (month in months) and (1 <= int(day) <= 31) and (len(year) == 4):
                month = int(months.index(month) + 1)
                day = int(day)
                #month = int(month)
                year = int(year)
                print(f'{year}-{month:02}-{day:02}')
                break

        except:
            pass

    except:
        pass
