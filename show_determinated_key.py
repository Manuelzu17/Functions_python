def palabras_con_todas_vocales(cadenas):
    vocales = set('aeiou')
    result = []
    for cadena in cadenas:
        if all(v in cadena.lower() for v in vocales):
            result.append(cadena)
    return result

word_list = ["hello", "algorithm", "education", "aeroplane", "time", "outrageous", "unique", "orange", "jupiter"]
vowel_words = palabras_con_todas_vocales(word_list)
print(vowel_words)
