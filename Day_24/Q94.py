def compress_string(s):
    if len(s) == 0:
        return ""

    result = ""
    count = 1
    prev = s[0]

    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            result += prev + str(count)
            prev = s[i]
            count = 1

    result += prev + str(count)
    return result


string = input("Enter a string: ")
print("Compressed string is:", compress_string(string))