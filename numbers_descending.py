def sort_numbers_reverse(numbers):
    return sorted(numbers, reverse=True)
#The function takes a list of numbers as argument and uses the sorted() function to sort them in descending order. The reverse=True argument indicates that the list should be sorted in descending order instead of ascending (which is the default option). The function returns the list sorted in descending order.
numbers = [8, 5, 3, 1, 7, 9, 10, 2, 4, 6]
sum_squares = sort_numbers_reverse(numbers)
print(sum_squares)
