def find_length(s):
    count = 0
    for ch in s:
        count += 1
    return count


string = input("Enter a string: ")
print("Length of the string is:", find_length(string))