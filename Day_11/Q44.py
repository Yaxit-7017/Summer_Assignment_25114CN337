def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial = factorial * i
    return factorial

num = int(input("Enter a number: "))

result = find_factorial(num)
print("Factorial of", num, "=", result)