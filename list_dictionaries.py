def ordenar_por_edad(lista):
    return sorted(lista, key=lambda x: x['edad'])
personas = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'Ana', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 20},
    {'nombre': 'María', 'edad': 25}
]
print(ordenar_por_edad(personas))
