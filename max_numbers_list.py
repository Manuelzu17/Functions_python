def max_numbers_in_lists(lists):
    """
    Given a list of lists, return a list with the maximum number in each list.
    """
    return [max(l) for l in lists]
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_numbers = max_numbers_in_lists(lists)
print(max_numbers)  # Output: [3, 6, 9]
