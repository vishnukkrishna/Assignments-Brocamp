def checkPalindrome(str):
    for i in range(0, len(str)):
        if str[i] == str[len(str) - i - 1]:
            return True
        return False


str1 = input("Enter you text: ")
oppsite=checkPalindrome(str1)

if oppsite:
    print("Palindrome")
else:
    print("Not a Palindrome")