def count_set_bits(n):
    count = 0
    
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2
    
    return count

num = int(input("Enter a number: "))
print(f"Number of set bits in {num} is: {count_set_bits(num)}")