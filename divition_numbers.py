def find_divisible_numbers(numbers, divisors):
    result = []
    for num in numbers:
        divisible = True
        for div in divisors:
            if num % div != 0:
                divisible = False
                break
        if divisible:
            result.append(num)
    return result
lista1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
lista2 = [2, 3, 5]

print(find_divisible_numbers(lista1, lista2))
