a=11
n=4
for i in range(n):
    a -= n-i
    for j in range(n-i):
        print(a+j,end=' ')
    print(" ")