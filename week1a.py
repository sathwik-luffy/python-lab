a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))

print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. remainder")

c = int(input("enter your choice: "))

if c == 1:
    print(a + b)

elif c == 2:
    print(a - b)

elif c == 3:
    print(a * b)

elif c == 4:
    print(a / b)

elif c == 5:
    print(a % b)

else:
    print("Invalid choice")