def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


n1 = int(input("Enter number of elements in first array: "))
arr1 = []
for i in range(n1):
    arr1.append(int(input("Enter element: ")))

n2 = int(input("Enter number of elements in second array: "))
arr2 = []
for i in range(n2):
    arr2.append(int(input("Enter element: ")))

print("Merged sorted array:", merge_sorted_arrays(arr1, arr2))