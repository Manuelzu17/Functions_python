def square_list(numbers):
    return list(map(lambda x: x**2, numbers))
numbers = [1, 2, 3, 4, 5]
squares = square_list(numbers)
#La función square_list() takes a list of numbers as an argument and returns a list of the squares of those numbers using the map() function. The lambda function lambda x: x**2 is used to calculate the square of each number in the list.
print(squares)
