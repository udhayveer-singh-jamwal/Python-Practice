# Write file
with open("data.txt", "w") as f:
    f.write("Learning Python File Handling\n")

# Append file
with open("data.txt", "a") as f:
    f.write("Intermediate Level\n")

# Read file
with open("data.txt", "r") as f:
    print(f.read())
