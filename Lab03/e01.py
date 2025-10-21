myString = "Hello World"

def string_to_dict(string):
    letter_dict = {}
    for char in string:
        letter_dict[char] = letter_dict.get(char, 0) + 1

    return letter_dict

print(string_to_dict(myString))