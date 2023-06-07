from abc import ABC, abstractmethod
class Calculator(ABC):

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def mul(self):
        pass
    @abstractmethod
    def div(self):
        pass
       
class Operations(Calculator):
   
    def add(self, num1,num2):
        print("Sum is : ", num1+num2)
    def sub(self, num1,num2):
        print("subtraction is : ", num1-num2)
    def mul(self, num1,num2):
        print("product is : ", num1*num2)
    def div(self, num1,num2):
        print("division is : ", num1/num2)

obj = Operations()
obj.add(
    int(input("Enter first number: ")),
    int(input("Enter second number: "))
)
obj.sub(
    int(input("Enter first number: ")),
    int(input("Enter second number: "))
)
obj.mul(
    int(input("Enter first number: ")),
    int(input("Enter second number: "))
)
obj.div(
    int(input("Enter first number: ")),
    int(input("Enter second number: "))
)