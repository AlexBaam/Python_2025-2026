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