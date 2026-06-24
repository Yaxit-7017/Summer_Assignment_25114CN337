def remove_duplicates(s):
    seen = {}
    result = ""

    for ch in s:
        if ch not in seen:
            seen[ch] = True
            result += ch

    return result


string = input("Enter a string: ")
print("String after removing duplicates:", remove_duplicates(string))