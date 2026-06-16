def find_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

arr = [1, 2, 3, 4, 5, 6]
target = 9
pair = find_pair_with_sum(arr, target)
print("Pair:", pair)