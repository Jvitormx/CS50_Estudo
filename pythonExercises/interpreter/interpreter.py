formula=input("Expression: ").strip()
x,y,z=formula.split(" ")

x1=float(x)
z1=float(z)

match y:
    case "+":
        c=x1+z1
    case "-":
        c=x1-z1
    case "*":
        c=x1*z1
    case "/":
        c=x1/z1

print(c)
