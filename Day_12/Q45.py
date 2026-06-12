def check_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

word = input("Enter a word or number: ")

if check_palindrome(word):
    print(word, "is a Palindrome")
else:
    print(word, "is Not a Palindrome")