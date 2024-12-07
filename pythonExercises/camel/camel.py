camel=input("camelCase: ")

for char in camel:
        if char.isupper()==True:
            new_char=char.lower()
            list=camel.split(char)
            list[0]+=("_"+new_char)
            save=''.join(list)
            camel=save
        else:
              continue

print(camel)




