# Password checker
password = input("Enter password: ")

if len(password) < 6:
    print("Weak password")
else:
    print("Strong password")
