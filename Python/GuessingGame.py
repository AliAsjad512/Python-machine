import random

def guess_number():
    """Number guessing game between 1-100"""
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
        
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\nGame Over! The number was {secret_number}")

# Run game
guess_number()