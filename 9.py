limit=int(input("Enter the size of array: "))
array_one=[]
print(f"Enter the {limit} value of array_one: ")

for i in range(limit):
    array_one.append(int(input()))
print(f'The  array is  :{array_one}')
array_two=array_one.copy()
array_two.append(int(input("Enter the values to be added: ")))

print(f'Array 1: {array_one}')
print(f'Array 2: {array_two}')