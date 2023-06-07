number=int(input("Enter a number from 1 to 7: "))
days={
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    7:"Saturday"
}
if number>=1 and number<=7 :
    print(days.get(number))
else :
    print("Invalid entry")