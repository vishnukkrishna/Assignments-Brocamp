array=[]
def getArray():
    size=int(input("Enter a size of an array: "))
    for i in range(0,size):
        value=int(input())
        array.append(value)

def displayArray():
    print("Your entered array is: ",array)

getArray()
displayArray()