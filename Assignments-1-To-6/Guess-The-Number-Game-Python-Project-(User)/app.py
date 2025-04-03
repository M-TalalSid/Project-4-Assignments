import random

def computer_guess(x):
    print("\n🎉 Welcome to the Number Guessing Game! 🎉")
    print("I'm here to guess your number and have fun with you! 😊 Let's get started!\n")

    low = 1
    high = x
    feedback = ''
    attempts = 0

    while feedback != 'c':
        if low > high:
            print("Oops, something went wrong. Let's try again! 😅")
            break

        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too low (L), too high (H), or correct (C)? ").lower()
        attempts += 1
        print(f"Attempt {attempts}! I'm trying my best! 💪")

        if feedback == "h":
            high = guess - 1
            print("Okay, I'll aim lower next time. Thanks for the hint! 😊")
        elif feedback == "l":
            low = guess + 1
            print("Got it, I'll try a higher number! Let's keep going! 😄")
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} in {attempts} attempts! 🎉")
            print("It was great playing with you! Hope you had fun! 😊")
            break

        if attempts == 5:
            print("Oh no, I've run out of attempts! 😞")
            print("But don't worry, we can always play again! Want to give it another try? 😊")
            break

# Start the game with a range up to 10
computer_guess(10)