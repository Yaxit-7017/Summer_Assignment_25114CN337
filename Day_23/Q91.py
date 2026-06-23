def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    return char_frequency(s1) == char_frequency(s2)


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if is_anagram(string1, string2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")