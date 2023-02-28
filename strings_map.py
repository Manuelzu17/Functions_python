def reverse_list_strings(strings):
    return list(map(lambda s: s[::-1], strings))
strings = ['hola', 'mundo', 'python']
reverse_strings = reverse_list_strings(strings)
#The function reverse_list_strings() takes a list of strings as an argument and returns a list of the same strings in reverse order using the map() function. The lambda function lambda s: s[::-1] is used to reverse each string in the list.
print(reverse_strings)
