def check_perfect(n):
    if n < 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    if total == n:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if check_perfect(num):
    print(num, "is a Perfect number")
else:
    print(num, "is Not a Perfect number")