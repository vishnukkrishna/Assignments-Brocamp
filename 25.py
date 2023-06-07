class CustomException(Exception):
    pass

try:
    print("1 - Biriyani \n2 - Mandhi \n3 - Ghee rice \n4 - Fried rice")
    input_num = int(input("Enter a number: "))
    if input_num == 1:
        raise CustomException
    elif input_num >4:
        print("Wrong choise")
    else:
        print("Thank you for Ordering")
       
except CustomException:
    print("Biriyani is not available right now")