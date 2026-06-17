def find_common_elements(arr1, arr2, arr3):
    set1 = set(arr1)
    set2 = set(arr2)
    result = []

    for num in arr3:
        if num in set1 and num in set2:
            result.append(num)

    return sorted(list(set(result)))

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
arr3 = [3, 5, 7, 8, 9]
result = find_common_elements(arr1, arr2, arr3)
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)
print("Common Elements:", result)