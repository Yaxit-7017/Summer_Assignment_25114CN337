start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Armstrong numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    digits = str(num)
    power = len(digits)
    total = 0
    for digit in digits:
        total = total + int(digit) ** power
    if total == num:
        print(num, end=" ")