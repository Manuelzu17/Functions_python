def Sort_even_and_odd(nums):
    pares = sorted([num for num in nums if num % 2 == 0])
    impares = sorted([num for num in nums if num % 2 != 0])
    return pares + impares

numbers = [5, 2, 3, 8, 6, 7, 4, 1]
print(Sort_even_and_odd(numbers))
