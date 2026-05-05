print("size of the first matrix")
r1 = int(input())
c1 = int(input())

print("size of the second matrix")
r2 = int(input())
c2 = int(input())

if c1 != r2:
    print("cannot be multiplied")
else:
    print("enter the numbers in first matrix")
    a = [[int(input()) for i in range(c1)] for j in range(r1)]

    print("enter the numbers in second matrix")
    b = [[int(input()) for i in range(c2)] for j in range(r2)]

    c = [[0 for i in range(c2)] for j in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                c[i][j] += a[i][k] * b[k][j]

    print("result matrix")
    for i in range(r1):
        for j in range(c2):
            print(c[i][j], end=" ")
        print()