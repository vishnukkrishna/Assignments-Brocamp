print("Enter the marks obtained from: ")
writtenText=int(input("Written text: "))
labExam=int(input("Lab exam: "))
assignment=int(input("Assignment: "))

grade=(writtenText*70)/100+(labExam*20)/100+(assignment*10)/100
print("Grade of the students: ",grade)