def is_palindrome(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return s == reversed_str


string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")