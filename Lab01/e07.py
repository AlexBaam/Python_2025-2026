"""Write a function that extract a number from a text (for example if the text is
 "An apple is 123 USD", this function will return 123, or if the text is
  "abc123abc" the function will extract 123).
The function will extract only the first number that is found."""

text = "abc123abc456"
number = ""
cont = True
index = 0

while cont:
    if text[index].isdigit():
        number += text[index]
    if index < len(text)-1 and text[index].isdigit() and text[index+1].isalpha():
        cont = False
    index += 1

print(number)