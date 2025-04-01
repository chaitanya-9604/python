import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while not guessed_correctly:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess < number_to_guess:
                print("Too low Try again.")
            elif guess > number_to_guess:
                print("Too high Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()