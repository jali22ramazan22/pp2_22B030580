import random

def play_game():
    # Generate a random number between 1 and 20
    number = random.randint(1, 20)

    # Loop until the user guesses the correct number
    while True:
        # Get a guess from the user
        guess = input("Guess a number between 1 and 20: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Check if the guess is correct, too low, or too high
        if guess == number:
            print("Congratulations, you guessed the number!")
            break
        elif guess < number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
