import csv

name = input("Enter your name: ")
mbl = input("Enter your mobile number: ")
mail = input("Enter email id: ")

obj = open("data.csv", "w", newline="")

wr = csv.writer(obj)

wr.writerow(["name", "mbl", "mail"])
wr.writerow([name, mbl, mail])

print("Successfully inserted")

obj.close()