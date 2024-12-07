while True:
    fraction=input("Fraction: ").split("/")
    try:
        x,y=fraction
    except ValueError:
        continue
    try:
        intx=int(x)
        inty=int(y)
    except ValueError:
        continue
    else:
        if(intx>inty):
            continue
        try:
            value=intx/inty
        except ZeroDivisionError:
            continue
        else:
            if value==1 or value==0.99:
                print("F")
                break
            elif value==0 or value==0.01:
                print("E")
                break
            else:
                print(f"{int(round(value*100))}%")
                break
