def main():
    while True:
        number=input("number: ")
        if number.isnumeric()==False or len(number)>10:
            continue
        else:
            number=list(number)
            for _ in range(len(number)):
                number[_]=int(number[_])

        print(create_phone_number(number))
        break


def create_phone_number(n):
    new_number=
    return n

main()