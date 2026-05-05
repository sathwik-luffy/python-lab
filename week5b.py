class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


num = 10

while True:

    try:
        my_num = int(input("Enter a number: "))

        if my_num < num:
            raise ValueTooSmallError

        elif my_num > num:
            raise ValueTooLargeError

        else:
            print("You have guessed the number successfully")
            break

    except ValueTooSmallError:
        print("Enter a bigger number")

    except ValueTooLargeError:
        print("Enter a smaller number")