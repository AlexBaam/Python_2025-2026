"""Write a function that counts how many words exists in a text.
 A text is considered to be form out of words that are separated by only ONE space.
For example: "I have Python exam" has 4 words."""

text = "I am Nicu and I have Python exam. Save me please!"

count = 0
for words in text.split(" "):
    count += 1

print(text)
print(count)