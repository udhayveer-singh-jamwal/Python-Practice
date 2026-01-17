class AgeError(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise AgeError("Age must be 18+")
else:
    print("Access granted")
