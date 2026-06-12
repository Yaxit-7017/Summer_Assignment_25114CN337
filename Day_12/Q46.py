def check_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for d in digits:
        total = total + int(d) ** power
    if total == n:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if check_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is Not an Armstrong number")