def main():
    print(result('Fraction: '))


def result(input_string):
    while True:
        foo = input(input_string)

        try:
            bar, baz = (foo.split('/'))
            bar = int(bar)
            baz = int(baz)

            if bar <= baz and bar >= 0 and baz != 0:
                answer = round(bar / baz * 100)
                if answer <= 1:
                    answer = 'E'
                elif answer >= 99:
                    answer = 'F'
                elif str(answer).isnumeric():
                    answer = f'{answer}%'
                return(answer)

        except (ValueError, ZeroDivisionError):
            main()


main()
