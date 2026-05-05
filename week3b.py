text = input("Enter a text : ")

text = text.lower()

words = text.split()

wordcount = {}

for i in words:

    if i in wordcount:
        wordcount[i] += 1

    else:
        wordcount[i] = 1


max_freq = max(wordcount.values())

print("Most frequent words")

for i in wordcount:

    if wordcount[i] == max_freq:
        print(i)

print("Frequency =", max_freq)