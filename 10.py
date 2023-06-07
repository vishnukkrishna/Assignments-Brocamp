def bubble_sort(limit,array):
    for i in range(0,limit):
        for j in range(0,(limit-i)-1):
            if (array[j] < array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    print("The sorted array is: " , array)

# Size of the array
limit=int(input("Enter the size of array: "))
array=[]
print("Enter the value of the array")
for i in range(limit):
    array.append(int(input()))
print("Your entered array is: ",array)
# Function called
bubble_sort(limit,array)
