n = int(input("Enter the term: "))

a = 0
b = 1

if n == 1:
    print("Fibonacci term is:", a)
elif n == 2:
    print("Fibonacci term is:", b)
else:
    for i in range(2, n):
        a, b = b, a + b
    print("Fibonacci term is:", b)