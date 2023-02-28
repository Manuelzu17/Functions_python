def sort_pares_impares(nums):
    pares = sorted([num for num in nums if num % 2 == 0])
    impares = sorted([num for num in nums if num % 2 != 0])
    return pares + impares

numeros = [5, 2, 3, 8, 6, 7, 4, 1]
print(sort_pares_impares(numeros))
