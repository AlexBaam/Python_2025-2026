stringX = "an by new hel si gator bl"
stringY = "hello im blue and my name is nicu and i was bitten by an aligator"

count = 0

for wordsY in stringY.split():
    for wordsX in stringX.split():
        if wordsY.startswith(wordsX):
            count = count + 1

print(count)