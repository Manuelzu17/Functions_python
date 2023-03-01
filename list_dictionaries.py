def sort_by_age(list):
    return sorted(list, key=lambda x: x['age'])
people = [
    {'name': 'Juan', 'age': 25},
    {'name': 'Ana', 'age': 30},
    {'name': 'Pedro', 'age': 20},
    {'name': 'María', 'age': 25}
]
print(sort_by_age(people))
