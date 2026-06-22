def count_words(s):
    count = 0
    in_word = False
    for ch in s:
        if ch != " " and not in_word:
            in_word = True
            count += 1
        elif ch == " ":
            in_word = False
    return count


sentence = input("Enter a sentence: ")
print("Number of words:", count_words(sentence))