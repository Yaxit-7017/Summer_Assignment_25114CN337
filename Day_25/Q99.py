def sort_names(names):
    n = len(names)
    for i in range(n):
        for j in range(n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    return names


n = int(input("Enter number of names: "))
names = []
for i in range(n):
    names.append(input("Enter name: "))

print("Names sorted alphabetically:", sort_names(names))