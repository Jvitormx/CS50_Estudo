import sys

cont=0

if(len(sys.argv)==2):
    if sys.argv[1].endswith(".py")==True:
        try:
            with open(sys.argv[1], "r") as file:
                for line in file:
                    if line.startswith("#")==True or "#" in line or line.startswith("'''")==True or line.lstrip()=="":
                        continue
                    else:
                        cont+=1
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
    else:
        print("Not a file")
        sys.exit(1)

elif len(sys.argv)>2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    print("Too few command-line arguments")
    sys.exit(1)

print(cont)
