import random

def welcome_message():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

def get_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def give_hint(guess, target):
    if guess < target:
        print("📉 Too low! Try a higher number.")
    elif guess > target:
        print("📈 Too high! Try a lower number.")
    else:
        print("✅ Correct! You guessed the number!")

def play_game():
    welcome_message()
    number_to_guess = get_random_number()
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = get_user_guess()
        attempts += 1

        if guess == number_to_guess:
            give_hint(guess, number_to_guess)
            print(f"🎉 You found the number in {attempts} attempts.")
            guessed_correctly = True
        else:
            give_hint(guess, number_to_guess)

# Start the game
play_game()
