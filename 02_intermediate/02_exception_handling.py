try:
    a = int(input("Enter number: "))
    print(100 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("No error")
finally:
    print("Program ended")
