l = list(map(int, input("Enter the elements: ").split()))

l.sort()
le = len(l)

mean = sum(l) / le
print("Mean =", mean)

if le % 2 == 0:
    median = (l[le // 2] + l[le // 2 - 1]) / 2
else:
    median = l[le // 2]

print("Median =", median)

d = {}

for i in l:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

max1 = max(d.values())

mode = []

for i in d:
    if d[i] == max1:
        mode.append(i)

print("Mode =", mode)