def reverse_number(n):
    n = str(n)
    n = n[::-1]
    n = int(n)
    return n

num = int(input("Enter a number: "))
result = reverse_number(num)
print("Reversed number:", result)