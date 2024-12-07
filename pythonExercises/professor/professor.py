import random
import sys


def main():
    score=0
    level=get_level()
    for _ in range(10):
        list=generate_integer(level)
        n1=int(list[0])
        n2=int(list[1])
        try:
            result=int(input(f"{n1} + {n2} = "))
        except ValueError:
            print("EEE")
            for _ in range(3):
                try:
                    result=int(input(f"{n1} + {n2} = "))
                except ValueError:
                    print("Value is not an integer")
                else:
                    if result!=(n1+n2):
                        continue
                    else:
                        score+=1
                        break
            if result!=(n1+n2):
                print(n1+n2)
        else:
            if result!=(n1+n2):
                print("EEE")
                for _ in range(3):
                    try:
                        result=int(input(f"{n1} + {n2} = "))
                    except ValueError:
                        print("Value is not an integer")
                    else:
                        if result!=(n1+n2):
                            continue
                        else:
                            score+=1
                            break
                if result!=(n1+n2):
                    print(n1+n2)
            else:
                score+=1
    print(f"Score={score}")


def get_level():
    while True:
        n=input("Level: ")
        if n=="1" or n=="2" or n=="3":
            return int(n)


def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        y=random.randint(0,9)

        numbers=[x,y]
        return numbers

    elif level==2:
        x_int=random.randint(10,99)

        y_int=random.randint(10,99)

        numbers=[x_int,y_int]
        return numbers

    elif level==3:
        x_int=random.randint(100,999)

        y_int=random.randint(100,999)

        numbers=[x_int,y_int]
        return numbers
    else:
        sys.exit()


if __name__ == "__main__":
    main()