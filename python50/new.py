text="eu amo vc"
words=text.split()

for word in words:
    print(word)

print()

for word in words:
    for c in word:
        print(c)

print()

for word in words:
    if "o" in word:
        print(word)

print()

for word in words[2:]:
    print(word)

print()




