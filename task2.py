import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0
    
    print("Guess the number between 1 and 100!")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the game
number_guessing_game()



