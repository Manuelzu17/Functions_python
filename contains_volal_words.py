def contains_all_vowels(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for word in words:
        if all(v in word.lower() for v in vowels):
            result.append(word)
    return result

words = ['queue', 'apple', 'one', 'euphoria', 'continuous', 'penguin', 'sequoia']
result = contains_all_vowels(words)
print(result)
