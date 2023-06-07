class arrayOperation:
    row=int(input("Enter no of rows: "))
    column=int(input("Enter no of columns: "))
    array_one = []
    array_two = []
    array_three = []

    def getArray(self):
        print("Enter 1st array elements: ")
        for i in range(self.row):
            temp = []
            for j in range(self.column):
                value=int(input())
                temp.append(value)
            self.array_one.append(temp)

        print("Enter 2nd array elements: ")
        for i in range(self.row):
            temp = []
            for j in range(self.column):
                value=int(input())
                temp.append(value)
            self.array_two.append(temp)

    def addArray(self):
        for i in range(self.row):
            temp = []
            for j in range(self.column):
                value = self.array_one[i][j] + self.array_two[i][j]
                temp.append(value)
            self.array_three.append(temp)

    def displayArray(self):
        print(self.array_three)

arr = arrayOperation()
arr.getArray()
arr.addArray()
arr.displayArray()