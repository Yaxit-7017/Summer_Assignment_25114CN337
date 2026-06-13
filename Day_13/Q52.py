n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

even_count = 0
odd_count = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Array is:", arr)
print("Even elements count =", even_count)
print("Odd elements count =", odd_count)