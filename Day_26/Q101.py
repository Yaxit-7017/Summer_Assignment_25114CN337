import random

def number_guessing_game():
    print("=== Number Guessing Game ===")
    low, high = 1, 100
    number = random.randint(low, high)
    attempts = 0
    max_attempts = 7

    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < low or guess > high:
            print(f"Please guess within {low}-{high}.")
        elif guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts left: {remaining}")
    else:
        print(f"Out of attempts! The number was {number}.")

if __name__ == "__main__":
    number_guessing_game()