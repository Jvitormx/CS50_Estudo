import sys

names=["Bill", "Charlie", "Fred", "Fred2", "Ron"]

name=input("Name: ")

if name in names:
        print(f"Here it is: {n}")
        sys.exit(0)

print("Not found...")
sys.exit(1)