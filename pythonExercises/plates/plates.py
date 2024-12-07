def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if "." in s or "," in s or " " in s:
        return False

    if len(s)<2 and len(s)>6:
        return False
    else:
        match len(s):
            case 2:
                if s[0:1]=="0":
                    return False
                else:
                    return True
            case 3:
                for char in s:
                    last=s[2:3]
                    if s[0:1]=="0":
                        return False
                    elif last.isalpha()==True:
                        if s[1:2].isnumeric()==True:
                            return False
                        else:
                            return True
                    else:
                        return True
            case 4:
                 for char in s:
                    last=s[3:4]
                    if s[0:1]=="0":
                        return False
                    elif last.isalpha()==True:
                        if s[1:3].isnumeric()==True:
                            return False
                        else:
                            return True
                    else:
                        return True
            case 5:
                  for char in s:
                    last=s[2:5]
                    for i in range(len(last)):
                        n2=last[1]
                        n3=last[2]
                        if s[0:1]=="0":
                            return False
                        elif n3.isalpha()==True or n2.isalpha()==True:
                            if n2.isnumeric()==True or n3.isnumeric()==True:
                                return False
                            else:
                                return True
                        else:
                            return True

            case 6:
                 for char in s:
                    last=s[3:6]
                    for i in range(len(last)):
                        n2=last[1]
                        n3=last[2]
                        if s[0:1]=="0":
                            return False
                        elif n3.isalpha()==True or n2.isalpha()==True:
                            if n2.isnumeric()==True or n3.isnumeric()==True:
                                return False
                            else:
                                return True
                        else:
                            return True



main()
