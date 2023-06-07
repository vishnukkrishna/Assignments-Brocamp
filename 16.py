def outer():
    def decorator():
        print("HELLO WORLD")
    return decorator

toPrint = outer()
toPrint()