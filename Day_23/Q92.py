def max_occurring_char(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    max_char = ""
    max_count = 0
    for ch, count in freq.items():
        if count > max_count:
            max_count = count
            max_char = ch

    return max_char, max_count


string = input("Enter a string: ")
ch, count = max_occurring_char(string)
print("Maximum occurring character is:", repr(ch), "with count", count)