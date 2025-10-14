def prob6():
    matrix =[]

    rows = int(input("Numar de randuri dorite: "))
    cols = int(input("Numar de coloane dorite: "))

    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            number = int(input("Numar dorit: "))
            row.append(number)
        matrix.append(row)

    rowImOn = 0;
    for i in matrix:
        for j in i:
            if rowImOn%2 ==0 and i[j]%2 ==1:
                i[j] = 'x'
            elif rowImOn%2 ==1 and i[j]%2 ==0:
                i[j] = 'x'
        rowImOn = rowImOn + 1

    print(matrix)

prob6()