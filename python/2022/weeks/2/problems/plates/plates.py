def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if not plate.isalnum():
        return False

    if not plate[0:2].isalpha():
        return False

    if not 2 <= len(plate) <= 6:
        return False

    for i in range(len(plate)):
        current_symbol = plate[i]

        if current_symbol.isdigit():
            if not plate[i:].isdigit():
                return False

            if current_symbol == '0':
                return False

            break

    return True


main()
