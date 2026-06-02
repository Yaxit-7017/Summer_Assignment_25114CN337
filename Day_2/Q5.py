num = int(input("Enter a number: "))

sum = 0

for digit in str(num):
    sum = sum + int(digit)

print("Sum of digits:", sum)