def find_duplicates(numbers):
    duplicates = set([x for x in numbers if numbers.count(x) > 1])
    return list(duplicates)
numbers = [1, 2, 3, 2, 4, 3, 5, 6, 5]
duplicates = find_duplicates(numbers)
print(duplicates) # Output: [2, 3, 5]
