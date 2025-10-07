"""Write a script that reads a string,
 then builds in memory and displays on the screen the string of characters obtained from the read
 string by removing all characters that are not letters."""

string = "M0y na12me is32 Ni3240cu"
newString = ""

print(string)

for letter in string:
    if not letter.isdigit():
        newString += letter

print(newString)