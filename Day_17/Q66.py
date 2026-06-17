def union_of_arrays(arr1, arr2):
    result = set()
    
    for num in arr1:
        result.add(num)
    
    for num in arr2:
        result.add(num)
    
    return sorted(list(result))

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
result = union_of_arrays(arr1, arr2)
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Union of Arrays:", result)