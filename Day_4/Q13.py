n = int(input("Enter how many terms: "))

a = 0
b = 1

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b