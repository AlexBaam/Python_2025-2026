squaredList = list()

def prob1():
    n = int(input("Give a number: "))
    squaredList.clear()
    
    squareNumber = lambda x: x * x
    
    for i in range (1,n+1):
        squaredList.append(squareNumber(i))

    output = ''
    for i in squaredList:
        output = output + str(i) + '_'

    print(output[0:-1])

prob1()