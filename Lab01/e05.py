"""Write a function that validates if a number is a palindrome."""

number = 1200021
stringNumber = f"{number}"

strLen = len(stringNumber)
i = 0
j = -1

isPalindrome = True

if strLen % 2 == 0:
    while i < strLen/2:
        if stringNumber[i] != stringNumber[j]:
            isPalindrome = False
            break
        i = i + 1
        j = j - 1
else:
    while i < strLen/2 - 1:
        if stringNumber[i] != stringNumber[j]:
            isPalindrome = False
            break
        i = i + 1
        j = j - 1

print(stringNumber)
print(isPalindrome)