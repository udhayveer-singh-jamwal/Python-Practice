sentence = "python is easy and python is powerful"
words = sentence.split()
count = {}

for w in words:
    count[w] = count.get(w, 0) + 1
print(count)
