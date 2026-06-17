def intersection_of_arrays(arr1, arr2):
    set1 = set(arr1)
    result = set()

    for num in arr2:
        if num in set1:
            result.add(num)

    return sorted(list(result))

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
result = intersection_of_arrays(arr1, arr2)
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Intersection of Arrays:", result)
