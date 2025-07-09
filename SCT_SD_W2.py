import random

def guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10...")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Invalid input! Please enter an integer.")

if __name__ == "__main__":
    guessing_game()
