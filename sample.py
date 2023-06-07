# list1 = [1,2,3,4,5,6,7]
# for i in (list1):
#     sum = sum  + list1[i]

# print(sum)
# defining a class  
class mySample():  
    # using the __init__() function  
    def __init__(self):  
        self.first = 10  
        self._second = 15  
        self.__third = 20  
  
# instantiating the class  
myObj = mySample()  
# printing the directory of the object  
print(dir(myObj))  