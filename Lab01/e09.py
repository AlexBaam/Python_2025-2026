stringCamelCase = "UpperCamelCaseString"
stringWithUnderscores = ""

for char in stringCamelCase:
    if char.isupper():
        stringWithUnderscores +=  "_" + char.lower()
    else:
        stringWithUnderscores += char

print(stringWithUnderscores)