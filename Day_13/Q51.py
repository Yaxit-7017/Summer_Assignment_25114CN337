n = int(input("Enter the size of array: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

largest = arr[0]
smallest = arr[0]

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]

print("Array is:", arr)
print("Largest element =", largest)
print("Smallest element =", smallest)