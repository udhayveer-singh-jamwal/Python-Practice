nums = [45, 12, 89, 33, 67]

largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)
