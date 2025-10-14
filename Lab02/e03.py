matrix = []
input_row = []

def my_union(firstList, secondList):
    firstSet = set(firstList)
    secondSet = set(secondList)

    newList = firstSet.union(secondSet)

    return list(newList)

def my_intersection(firstList, secondList):
    firstSet = set(firstList)
    secondSet = set(secondList)

    newList = firstSet.intersection(secondSet)

    return list(newList)

def prob3():
    n = int(input("Number of rows in matrix: "))

    for i in range(1,n+1):

        input_row.clear()
        row = input(f"Row {i}: ")

        for j in row.split():
            input_row.append(int(j))

        matrix.append(input_row.copy())

    set1 = []
    matrixLen = len(matrix)
    i = 0

    while i < matrixLen:
        set1 = my_union(set1, matrix[i])
        i = i + 1

    set2 = matrix[0].copy()
    j = 1

    while j < matrixLen:
        set2 = my_intersection(set2, matrix[j])
        j = j + 1

    output_tuple = (set1, set2)
    print(output_tuple)

prob3()