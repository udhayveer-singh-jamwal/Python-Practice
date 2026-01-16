def outer(msg):
    def inner():
        print(msg)
    return inner

hello = outer("Hello Python")
hello()
