def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


string = input("Enter a string: ")
v, c = count_vowels_consonants(string)
print("Number of vowels:", v)
print("Number of consonants:", c)