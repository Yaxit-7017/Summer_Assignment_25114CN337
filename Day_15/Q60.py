arr = [0, 1, 0, 3, 12, 0, 5]

print("Original array:", arr)

non_zeroes = []
zeroes = []

for i in arr:
    if i != 0:
        non_zeroes.append(i)
    else:
        zeroes.append(i)

result = non_zeroes + zeroes

print("After moving zeroes to end:", result)

