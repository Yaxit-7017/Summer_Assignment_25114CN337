def binary_to_decimal(b):
    b = str(b)
    decimal = 0
    power = 0
    
    for digit in reversed(b):
        decimal += int(digit) * (2 ** power)
        power += 1
    
    return decimal

num = input("Enter a binary number: ")
print(f"{num} in decimal is: {binary_to_decimal(num)}")