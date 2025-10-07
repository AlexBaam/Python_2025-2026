string = "M0y na12me is32 Ni3240cu"
newString = ""

print(string)

for letter in string:
    if not letter.isdigit():
        newString += letter

print(newString)