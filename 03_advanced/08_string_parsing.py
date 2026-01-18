text = "Name:John,Age:25,City:Delhi"

data = {}
for item in text.split(","):
    key, value = item.split(":")
    data[key] = value

print(data)
