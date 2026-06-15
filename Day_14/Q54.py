arr = [10, 20, 30, 20, 40, 20, 50, 10]
target = int(input("Enter number to find frequency: "))

count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count = count + 1

print("Frequency of", target, "is", count)