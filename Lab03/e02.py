myFirstString = "Hello World"
mySecondString = "Hello world"

def string_to_dict(string):
    letter_dict = {}
    for char in string:
        letter_dict[char] = letter_dict.get(char, 0) + 1

    return letter_dict

myFirstDict = string_to_dict(myFirstString)
mySecondDict = string_to_dict(mySecondString)

myThirdDict = {"A": {}, "B": {}}
myThirdDict.update({"A": myFirstDict})
myThirdDict.update({"B": mySecondDict})

myForthDict = {"A": {}, "B": {}}
myForthDict.update({"A": mySecondDict})
myForthDict.update({"B": myFirstDict})

print(myFirstDict)
print(mySecondDict)
print(myThirdDict)
print(myForthDict)

def compare_dict(dict1, dict2):
    for key in dict1:
        if key not in dict2:
            return False
        elif dict1[key] != dict2[key]:
            return False

    return True

print('Compare between first and second:', compare_dict(myFirstDict, mySecondDict))

print('Compare between first and third:', compare_dict(myFirstDict, myThirdDict))

print('Compare between third and third:', compare_dict(myThirdDict, myThirdDict))

print('Compare between first and fourth:', compare_dict(myThirdDict, myForthDict))