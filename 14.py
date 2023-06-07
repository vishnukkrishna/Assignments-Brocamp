def number():
    return lambda x: x+x

double= number()
print(double(int(input("Enter a digit to double: "))))