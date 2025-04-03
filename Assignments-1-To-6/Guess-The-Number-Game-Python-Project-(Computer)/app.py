import random

def get_valid_guess(x):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if 1 <= guess <= x:
                return guess
            else:
                print(f"Please guess a number between 1 and {x}.")
        except ValueError:
            print("Please enter a valid integer.")

def play_game(x, attempts_limit):
    random_number = random.randint(1, x)
    attempts = 0
    while True:
        print(f"\nAttempts left: {attempts_limit - attempts}")
        guess = get_valid_guess(x)
        attempts += 1
        if guess == random_number:
            print(f"\n🎉 Congratulations! You guessed it right in {attempts} attempts! 🏆")
            return (True, attempts)
        elif attempts == attempts_limit:
            print("\n💀 Game Over! Your attempt limit has exceeded. Try again next time! ❌")
            see_correct = input("Do you want to see the correct number? (yes/no): ").lower()
            if see_correct == "yes":
                print(f"The correct number was {random_number}.")
            return (False, attempts)
        else:
            if guess > random_number:
                print("\n📈 Too high! Try again. ⬆")
            else:
                print("\n📉 Too low! Try again. ⬇")

def main():
    print("🎯 Welcome to the Guessing Number Game! 🎯")
    
    while True:
        try:
            x = int(input("Enter the upper limit of the range (must be at least 1): "))
            if x < 1:
                print("The upper limit must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the upper limit.")
    
    while True:
        try:
            attempts_limit = int(input("Enter the number of attempts allowed (must be at least 1): "))
            if attempts_limit < 1:
                print("The number of attempts must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of attempts.")
    
    best_score = float('inf')
    play_again = "yes"
    while play_again.lower() == "yes":
        success, attempts_taken = play_game(x, attempts_limit)
        if success and attempts_taken < best_score:
            best_score = attempts_taken
        play_again = input("Do you want to play again? (yes/no): ")
    
    if best_score != float('inf'):
        print(f"Your best score is {best_score} attempts.")
    else:
        print("You didn't guess correctly in any game.")

if __name__ == "__main__":
    main()