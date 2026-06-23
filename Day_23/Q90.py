def first_repeating(s):
    seen = {}
    for ch in s:
        if ch in seen:
            return ch
        seen[ch] = True
    return None


string = input("Enter a string: ")
result = first_repeating(string)
if result:
    print("First repeating character is:", result)
else:
    print("No repeating character found")