num = input("Enter a number: ")

power = len(num)

total = 0

for digit in num:
    total = total + int(digit) ** power

if total == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")