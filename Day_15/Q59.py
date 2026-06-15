arr = [1, 2, 3, 4, 5]
k = 2

print("Original array:", arr)

k = k % len(arr)

rotated = arr[-k:] + arr[:-k]

print("Right rotated by", k, ":", rotated)