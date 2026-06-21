def reverse_string(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str


string = input("Enter a string: ")
print("Reversed string is:", reverse_string(string))