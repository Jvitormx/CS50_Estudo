def main():
    height=get_height()
    for i in range(height):
        print("#"*4)


def get_height():
    while True:
        try:
            n=int(input("Height: "))
        except ValueError:
            print("Oooo")
        else:
            if n>0:
                return n

main()