nums = [10, 40, 20, 50, 30]
largest = second = nums[0]

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n
print("Second Largest:", second)
