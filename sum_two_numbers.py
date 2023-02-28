def sum_pairs(numbers):
    pairs = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] in numbers:
                pairs.add(numbers[i] + numbers[j])
    return list(pairs)
numbers = [1, 3, 5, 7, 9, 11, 12, 15, 16]
result = sum_pairs(numbers)
print(result)  
