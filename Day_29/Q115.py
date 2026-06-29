def display_length(s):
    print(f"Length of string: {len(s)}")

def to_upper(s):
    print(f"Uppercase: {s.upper()}")

def to_lower(s):
    print(f"Lowercase: {s.lower()}")

def reverse_string(s):
    print(f"Reversed string: {s[::-1]}")

def check_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")

def count_words(s):
    words = s.split()
    print(f"Word count: {len(words)}")

def replace_substring(s):
    old = input("Enter substring to replace: ")
    new = input("Enter new substring: ")
    print(f"Result: {s.replace(old, new)}")

def find_substring(s):
    sub = input("Enter substring to find: ")
    if sub in s:
        print(f"Substring found at index {s.find(sub)}")
    else:
        print("Substring not found")

def concatenate_string(s):
    s2 = input("Enter another string: ")
    print(f"Concatenated string: {s + s2}")

def main():
    while True:
        print("\n----- String Operations Menu -----")
        s = input("Enter a string: ")
        print("1. Display Length")
        print("2. Convert to Uppercase")
        print("3. Convert to Lowercase")
        print("4. Reverse String")
        print("5. Check Palindrome")
        print("6. Count Vowels and Consonants")
        print("7. Count Words")
        print("8. Replace Substring")
        print("9. Find Substring")
        print("10. Concatenate String")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            display_length(s)
        elif choice == '2':
            to_upper(s)
        elif choice == '3':
            to_lower(s)
        elif choice == '4':
            reverse_string(s)
        elif choice == '5':
            check_palindrome(s)
        elif choice == '6':
            count_vowels_consonants(s)
        elif choice == '7':
            count_words(s)
        elif choice == '8':
            replace_substring(s)
        elif choice == '9':
            find_substring(s)
        elif choice == '10':
            concatenate_string(s)
        elif choice == '11':
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()