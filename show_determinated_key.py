def words_with_all_vowels(strings):
    vowels = set('aeiou')
    result = []
    for string in strings:
        if all(v in string.lower() for v in vowels):
            result.append(string)
    return result

word_list = ["hello", "algorithm", "education", "aeroplane", "time", "outrageous", "unique", "orange", "jupiter"]
vowel_words = words_with_all_vowels(word_list)
print(vowel_words)
