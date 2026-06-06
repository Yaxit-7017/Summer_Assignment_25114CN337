def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    
    return binary

num = int(input("Enter a decimal number: "))
print(f"{num} in binary is: {decimal_to_binary(num)}")