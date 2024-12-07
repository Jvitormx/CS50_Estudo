import sys

values=[]
keys=[]

while True:
    try:
        item=input().upper().strip()
        values.append(item)
    except EOFError:
        if len(values)==0:
            sys.exit()

        values.sort()
        for _ in range(len(values)):
            key=values.count(values[_])
            if _>=1:
                if values[_-1]==values[_]:
                    continue
                else:
                    keys.append(key)
            else:
                keys.append(key)
            set_values=list(set(values))
            set_values.sort()
        for _ in range(len(set_values)):
            print(keys[_],set_values[_])
        sys.exit()

