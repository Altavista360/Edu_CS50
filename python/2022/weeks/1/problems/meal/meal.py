def main():
    time = input('What time is it? ').strip()
    if convert(time) >= 7.0 and convert(time) <= 8.0: # 07:00 - 08:00
        print('breakfast time')
    elif convert(time) >= 12.0 and convert(time) <= 13.0: # 12:00 - 13:00
        print('lunch time')
    elif convert(time) >= 18.0 and convert(time) <= 19.0: # 18:00 - 19:00
        print('dinner time')


def convert(time):
    hours_time, minutes_time = time.split(":")
    hours_time = float(hours_time)
    minutes_time = float(minutes_time) / 60
    return hours_time + minutes_time


if __name__ == "__main__":
    main()
