def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum is: ", total)

sum_numbers(1,2,3,4)
sum_numbers(8,20,2)
sum_numbers(12.5,3.147,98.1)
sum_numbers(1.1,2.2,5.5)