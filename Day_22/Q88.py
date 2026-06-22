def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
    return result


string = input("Enter a string: ")
print("String without spaces:", remove_spaces(string))