n = input("Enter a number: ")

count = 0
for char in n:
    if char.isdigit():
        count += 1

print(f"Number of digits = {count}")