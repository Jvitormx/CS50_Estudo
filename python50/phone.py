people={
    "Carter":"7777",
    "David":"OOO88"
}

name=input("Name: ")
if name in people:
    number=people[name]
    print(f"Number of {name} is {number}")