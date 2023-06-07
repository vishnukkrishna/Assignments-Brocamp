row =int(input("Enter the number of rows: "))
column =int(input("Enter the numbers column: "))

print("Enter the values for first array: ")
array1 = []
for i in range(row):
    temp = []
    for j in range(column):
        values = int(input())
        temp.append(values)
    array1.append(temp)

print("Enter the values for first array: ")
array2 = []
for i in range(row):
    temp = []
    for j in range(column):
        values = int(input())
        temp.append(values)
    array2.append(temp)

array3 = []
print("Sum of 2 arrays is: ")
for i in range(row):
    temp = []
    for j in range(column):
        values = array1[i][j] + array2[i][j]
        temp.append(values)
    array3.append(temp)
print(array3)
