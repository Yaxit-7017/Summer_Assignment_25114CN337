def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    doubled = s1 + s1

    n = len(s2)
    m = len(doubled)
    for i in range(m - n + 1):
        match = True
        for j in range(n):
            if doubled[i + j] != s2[j]:
                match = False
                break
        if match:
            return True
    return False


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if is_rotation(string1, string2):
    print(string2, "is a rotation of", string1)
else:
    print(string2, "is not a rotation of", string1)