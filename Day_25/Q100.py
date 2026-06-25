def sort_words_by_length(words):
    n = len(words)
    for i in range(n):
        for j in range(n - i - 1):
            if len(words[j]) > len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    return words


sentence = input("Enter a sentence: ")
words = sentence.split()
print("Words sorted by length:", sort_words_by_length(words))