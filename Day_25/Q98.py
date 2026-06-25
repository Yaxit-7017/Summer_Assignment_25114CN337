def find_common_characters(s1, s2):
    common = ""
    for ch in s1:
        if ch in s2 and ch not in common:
            common += ch
    return common


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print("Common characters:", find_common_characters(string1, string2))