obj = open("data.txt", "r")

text = obj.read()

lc = uc = sc = vc = nc = 0
wc = 1

print("Text is\n", text)

for i in text:

    if i in "aeiouAEIOU":
        vc += 1

    elif i.isupper():
        uc += 1

    elif i in "0123456789":
        nc += 1

    elif i == " ":
        sc += 1
        wc += 1

print(f"No of vowels are {vc}")
print(f"No of spaces are {sc}")
print(f"No of words are {wc}")
print(f"No of uppercase letters are {uc}")
print(f"No of numerical values are {nc}")

obj.close()