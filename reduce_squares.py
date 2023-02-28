from functools import reduce

def sum_of_squares(numbers):
    return reduce(lambda acc, n: acc + n**2, numbers, 0)
#The function sum_of_squares() takes a list of numbers as an argument and returns the sum of the squares of those numbers using the reduce() function. The lambda function lambda acc, n: acc + n**2 is used to calculate the sum of the squares of the numbers in the list.
numbers = [1, 2, 3, 4, 5]
sum_squares = sum_of_squares(numbers)
print(sum_squares)
