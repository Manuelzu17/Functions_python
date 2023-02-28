def strings_with_s(strings):
    return list(filter(lambda s: 's' in s, strings))
strings = ['hola', 'mundo', 'python', 'silla', 'sabana']
# The function strings_with_s() takes a list of strings as an argument and returns a list of strings that contain the letter 's' using the filter() function. The lambda function lambda s: 's' in s is used to filter only the strings that contain the letter 's' in the list.
s_strings = strings_with_s(strings)
print(s_strings)
