n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

total = 0

for i in range(n):
    total = total + arr[i]

average = total / n

print("Array is:", arr)
print("Sum =", total)
print("Average =", average)