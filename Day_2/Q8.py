num = input("Enter a number: ")

reversed_num = num[::-1]

if num == reversed_num:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")