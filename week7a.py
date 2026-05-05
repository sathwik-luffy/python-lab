stack = []

ch = 1

print("Menu")
print("1. Push  2. Pop  3. Display")

max_size = int(input("Enter size of stack: "))

while ch == 1:

    c = int(input("Enter your choice: "))

    if c == 1:

        if len(stack) == max_size:
            print("Stack is full, cannot push items into stack")

        else:
            n = int(input("Enter element to be inserted: "))
            stack.append(n)

            print("Length is", len(stack))
            print("Stack is", stack)

    elif c == 2:

        if stack == []:
            print("Stack is empty, cannot remove items from stack")

        else:
            print("Element removed from stack is", stack.pop())

    elif c == 3:

        print("Stack to be displayed:", stack)

    else:
        print("Invalid choice")

    ch = int(input("Continue (1/0): "))