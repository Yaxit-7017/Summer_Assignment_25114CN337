def to_uppercase(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result


string = input("Enter a string: ")
print("Uppercase string is:", to_uppercase(string))