limit=int(input("Enter the limit: "))
for i in range(0, limit):
    num=1
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1

    print("\n")