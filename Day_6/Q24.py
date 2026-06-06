def power(x, n):
    result = 1
    
    for i in range(n):
        result *= x
    
    return result

x = int(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))
print(f"{x}^{n} = {power(x, n)}")