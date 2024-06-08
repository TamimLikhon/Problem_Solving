def reorder_sentence_and_remove_numbers(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: int(''.join(filter(str.isdigit, word))))
    cleaned_words = [''.join(filter(str.isalpha, word)) for word in sorted_words]
    return ' '.join(cleaned_words)

s = "is2 sentence4 This1 a3"
result = reorder_sentence_and_remove_numbers(s)
print(result) 
