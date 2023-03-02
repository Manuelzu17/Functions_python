import itertools

def sum_pairs(numbers):
    pairs = set()
    for i, j in itertools.combinations(numbers, 2):
        if i + j in numbers:
            pairs.add(i + j)
    return list(pairs)

numbers = [1, 3, 5, 7, 9, 11, 12, 15, 16]
result = sum_pairs(numbers)
print(result)

