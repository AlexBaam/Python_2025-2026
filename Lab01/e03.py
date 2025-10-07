"""Write a script where you process 2 strings, x and y.
 The strings consist of words (lowercase letters) separated by spaces.
 Determine how many words in x are prefixes of any word in y."""

stringX = "an by new hel si gator bl"
stringY = "hello im blue and my name is nicu and i was bitten by an aligator"

count = 0

for wordsY in stringY.split():
    for wordsX in stringX.split():
        if wordsY.startswith(wordsX):
            count = count + 1

print(count)