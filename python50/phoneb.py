import csv

file=open("phone.csv","a")

name=input("Name: ")
number=input("Cod: ")

writer=csv.DictWriter(file, fieldnames)
writer.writerow([name, number])

file.close()