def display(arr):
    if not arr:
        print("Array is empty")
    else:
        print("Array elements:", arr)

def insert_element(arr):
    val = input("Enter value to insert: ")
    pos = input("Enter position (index, leave blank for end): ")
    if pos.strip() == "":
        arr.append(val)
    else:
        try:
            pos = int(pos)
            arr.insert(pos, val)
        except ValueError:
            print("Invalid position")
    print("Element inserted")

def delete_element(arr):
    if not arr:
        print("Array is empty")
        return
    val = input("Enter value to delete: ")
    if val in arr:
        arr.remove(val)
        print("Element deleted")
    else:
        print("Value not found in array")

def search_element(arr):
    val = input("Enter value to search: ")
    if val in arr:
        print(f"Element found at index {arr.index(val)}")
    else:
        print("Element not found")

def sort_array(arr):
    try:
        numeric_arr = [float(x) for x in arr]
        numeric_arr.sort()
        arr.clear()
        arr.extend([str(int(x)) if x == int(x) else str(x) for x in numeric_arr])
    except ValueError:
        arr.sort()
    print("Array sorted")

def reverse_array(arr):
    arr.reverse()
    print("Array reversed")

def sum_array(arr):
    try:
        total = sum(float(x) for x in arr)
        print(f"Sum of elements: {total}")
    except ValueError:
        print("Error: Array contains non-numeric values")

def max_min(arr):
    try:
        numeric_arr = [float(x) for x in arr]
        print(f"Maximum: {max(numeric_arr)}")
        print(f"Minimum: {min(numeric_arr)}")
    except ValueError:
        print("Error: Array contains non-numeric values")

def main():
    arr = []
    while True:
        print("\n----- Array Operations Menu -----")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Search Element")
        print("5. Sort Array")
        print("6. Reverse Array")
        print("7. Sum of Elements")
        print("8. Max and Min")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            display(arr)
        elif choice == '2':
            insert_element(arr)
        elif choice == '3':
            delete_element(arr)
        elif choice == '4':
            search_element(arr)
        elif choice == '5':
            sort_array(arr)
        elif choice == '6':
            reverse_array(arr)
        elif choice == '7':
            sum_array(arr)
        elif choice == '8':
            max_min(arr)
        elif choice == '9':
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()