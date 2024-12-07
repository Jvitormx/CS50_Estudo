def main():
    greeting=input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting=greeting.lower().strip()
    list=greeting.split(" ")
    first=list[0]
    position=greeting.find("h")

    if first=="hello," or first=="hello":
        return 0
    elif position==0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
