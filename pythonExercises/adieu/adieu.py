import inflect
p = inflect.engine()
names=[]

while True:
    try:
        name=input()
        names.append(name)
    except EOFError:
        if len(names)==1:
            print(f"Adieu, adieu, to {names[0]}")
            break
        else:
            names=p.join(names)
            print(f"Adieu, adieu, to {names}")
            break
