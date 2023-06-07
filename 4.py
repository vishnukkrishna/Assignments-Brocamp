# mark=float(input("Enter your mark: "))
# if mark<50:
#     print("Fail")
# elif mark>=50 and mark<=100:
#     print("Pass")
# else:
#     print("Invalided Mark")
#

# setx = {"unknown", 1.100, "hi"}
# for i in setx:
#     print(i)

# def message_decorator(func):
#     def inner():
#         print("Hello, Message before Execution")
#
#         func()
#         print("Hello, Message After Execution")
#
#     return inner
#
#
# def new_function():
#     print("We declare inside the function !!")
#
#
# new_function = message_decorator(new_function)
# new_function()

# defining a class
class mySample:
    # using the __init__() function
    def __init__(self):
        self.first = 10
        # self._second = 15
        # self.__third = 20

    # instantiating the class


myObj = mySample()
# printing the directory of the object
print(dir(myObj))