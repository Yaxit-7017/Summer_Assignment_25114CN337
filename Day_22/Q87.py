def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


string = input("Enter a string: ")
result = char_frequency(string)
for ch, count in result.items():
    print(repr(ch), ":", count)