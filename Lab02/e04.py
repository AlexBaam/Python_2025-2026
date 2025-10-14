def prob4():
    count = int(input("Numar de perechi dorite: "))
    sum = int(input("Suma dorita: "))

    bigList = [(x, y) for x in range(1, sum) for y in range(1, sum) if (x + y) % sum == 0]

    print(bigList[0:count])

prob4()