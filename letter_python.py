def same_letter_words(words_list):
    return list(filter(lambda word: word[0].lower() == word[-1].lower(), words_list))
words = ["Ana", "Araña", "Bola", "Casa", "Eva"]
print(same_letter_words(words))
