example = {'start': 'a','b': 'a','a': '6','6': 'z','x': '2','z': '2','2': '2','y': 'start'}

def loop(mapping):
    checking_set = set()
    result = []

    start_key = mapping["start"]

    while start_key not in checking_set:
        checking_set.add(start_key)
        result.append(start_key)
        start_key = mapping[start_key]

    return result

print(loop(example))