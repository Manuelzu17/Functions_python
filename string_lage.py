from functools import reduce


def longest_string(strings):
    return reduce(lambda x, y: x if len(x) > len(y) else y, strings)


strings = ['Hola', 'Hello', 'Bonjour', 'Ciao']
# The function longest_string() takes a list of strings as an argument and returns the longest string using the reduce() function. The lambda function lambda x, y: x if len(x) > len(y) else y is used to compare two strings and return the longest string. The reduce() function applies this lambda function to the list of strings and returns the longest string.
longest = longest_string(strings)
print(longest)
