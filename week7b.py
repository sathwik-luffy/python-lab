queue = []

while True:

    print("\nQueue Menu")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Top element")
    print("4. Display all elements")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        item = int(input("Enter element: "))
        queue.append(item)

        print(f"{item} added to queue")

    elif choice == 2:

        if len(queue) == 0:
            print("Queue is empty")

        else:
            print("Removed:", queue.pop(0))

    elif choice == 3:

        if len(queue) == 0:
            print("Queue is empty")

        else:
            print("Top element is:", queue[-1])

    elif choice == 4:

        if len(queue) == 0:
            print("Queue is empty")

        else:
            print("All elements:", queue)

    elif choice == 5:

        print("Quitting program")
        break

    else:
        print("Invalid input")