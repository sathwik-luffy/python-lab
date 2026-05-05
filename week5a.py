n = int(input("Enter the number: "))
a = int(input("Enter the number 2: "))

try:
    print(n / a)

except ZeroDivisionError:
    print("There is an error")
    print("The number cannot be divisible by 0")

else:
    print("There is no error")

finally:
    print("Program executed successfully")