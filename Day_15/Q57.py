arr = [1, 2, 3, 4, 5]
reversed_arr = []

for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print(reversed_arr)