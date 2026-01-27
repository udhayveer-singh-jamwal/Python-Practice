nums = [1, 2, 3, 2, 4, 1]
duplicates = []

for n in nums:
    if nums.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

print("Duplicates:", duplicates)
