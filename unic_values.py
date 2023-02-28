def unique_values_by_key(dict_list, key):
    unique_values = set()
    for d in dict_list:
        if key in d:
            unique_values.add(d[key])
    return list(unique_values)
dict_list = [
    {'name': 'John', 'age': 25},
    {'name': 'Mary', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 35},
    {'name': 'John', 'age': 28},
]
data = [    {'name': 'John', 'age': 25},    {'name': 'Jane', 'age': 30},    {'name': 'Bob', 'age': 25},    {'name': 'Mary', 'age': 35},    {'name': 'Alice', 'age': 30}]

unique_ages = unique_values_by_key(data, 'age')
print(unique_ages) # Output: [25, 30, 35]
