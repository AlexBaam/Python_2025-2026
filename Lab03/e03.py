myFirstSet = {1, 2, 3, 4, 5}
mySecondSet = {2, 3, 4, 5, 6}
myThirdSet = {1, 2, 3, 4, 5, 6}
myFourthSet = {4, 5, 6, 7, 8}

listOfSets = [myFirstSet, mySecondSet, myThirdSet, myFourthSet]

def multiple_sets_operations(list_of_sets):
    result = {}

    for set1 in list_of_sets:
        for set2 in list_of_sets:
            if set1 != set2:
                result[f"{set1} | {set2}"] = set1.union(set2)
                result[f"{set1} & {set2}"] = set1.intersection(set2)
                result[f"{set1} - {set2}"] = set1.difference(set2)
                result[f"{set2} - {set1}"] = set2.difference(set1)

    return result

operation_result = multiple_sets_operations(listOfSets)

for a in operation_result.items():
    print(a)
