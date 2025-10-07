stringCamelCase = "UpperCamelCaseString"
stringWithUnderscores = ""
index = 0

for char in stringCamelCase:
    if char.isupper() and index == 0:
        stringWithUnderscores += char.lower()
    elif char.isupper():
        stringWithUnderscores +=  "_" + char.lower()
    else:
        stringWithUnderscores += char
    index += 1

print(stringCamelCase)
print(stringWithUnderscores)