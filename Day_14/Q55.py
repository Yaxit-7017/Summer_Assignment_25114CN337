arr = [10, 50, 30, 40, 20]

largest = -1
second_largest = -1

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Array is:", arr)
print("Second largest element is:", second_largest)