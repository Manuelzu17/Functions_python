import functools

def find_divisible_numbers(numbers, divisors):
    result = []
    for num in numbers:
        if functools.reduce(lambda x, y: x and y, map(lambda x: num % x == 0, divisors)):
            result.append(num)
    return result

lista1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
lista2 = [2, 3, 5]

print(find_divisible_numbers(lista1, lista2))

