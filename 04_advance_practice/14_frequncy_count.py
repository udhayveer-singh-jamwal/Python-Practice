data = ["a", "b", "a", "c", "b", "a"]
freq = {}

for item in data:
    freq[item] = freq.get(item) + 1

print(freq)
