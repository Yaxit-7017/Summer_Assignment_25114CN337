def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

arr = [1, 2, 3, 2, 4, 3, 5, 1, 6]
result = remove_duplicates(arr)
print("Original array:", arr)
print("After removing duplicates:", result)