arr = [10, 20, 30, 20, 40, 10, 50]

print("Array is:", arr)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[i], "is duplicate")
            break