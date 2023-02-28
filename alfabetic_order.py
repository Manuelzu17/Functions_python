def sort_strings_ignore_case(strings):
    return sorted(strings, key=str.lower)
strings = ['start', 'hola', 'mundo', 'python', 'silla', 'sabana']
#The sorted() function sorts the strings list alphabetically using the key function to define the sort key. In this case, the sort key is the lowercase version of each string, obtained using the str.lower() function. This makes uppercase and lowercase letters ignored during the sorting process.
sort_strings_ignore_case = sort_strings_ignore_case(strings)
print(sort_strings_ignore_case)