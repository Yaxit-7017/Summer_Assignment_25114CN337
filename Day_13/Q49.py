n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Array is:", arr)