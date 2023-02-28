def even_numbers(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = even_numbers(numbers)
#The function even_numbers() takes a list of numbers as an argument and returns a list of even numbers using the filter() function. The lambda function lambda n: n % 2 == 0 is used to filter only the even numbers in the list.
print(even)
