a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = a
temp = b

while temp != 0:
    gcd, temp = temp, gcd % temp

lcm = (a * b) // gcd

print("LCM is:", lcm)