def find_longest_word(s):
    longest = ""
    current = ""

    for ch in s:
        if ch != " ":
            current += ch
        else:
            if len(current) > len(longest):
                longest = current
            current = ""

    if len(current) > len(longest):
        longest = current

    return longest


sentence = input("Enter a sentence: ")
print("Longest word is:", find_longest_word(sentence))