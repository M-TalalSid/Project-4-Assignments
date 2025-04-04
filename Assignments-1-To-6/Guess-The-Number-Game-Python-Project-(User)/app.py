import random

def computer_guess(x):
    print("\n🎉 Welcome To The Number Guessing Game ! 🎉")
    print("I'm Here To Guess Your Number And Have Fun With You ! 😊 Let's Get Started !\n")

    low = 1
    high = x
    feedback = ''
    attempts = 0

    while feedback != 'c':
        if low > high:
            print("Oops, Something Went Wrong. Let's Try Again ! 😅")
            break

        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too low (L), too high (H), or correct (C)? ").lower()
        attempts += 1
        print(f"Attempt {attempts}! I'm Trying My Best ! 💪")

        if feedback == "h":
            high = guess - 1
            print("Okay, I'll Aim Lower Next Time. Thanks For The Hint ! 😊")
        elif feedback == "l":
            low = guess + 1
            print("Got it, I'll Try A Higher Number ! Let's Keep Going ! 😄")
        elif feedback == "c":
            print(f"Yay ! I Guessed Your Number {guess} In {attempts} Attempts ! 🎉")
            print("It Was Great Playing With You ! Hope You Had Fun ! 😊")
            break

        if attempts == 5:
            print("Oh No, I've Run Out Of Attempts! 😞")
            print("But Don't Worry, We Can Always Play Again ! Want To Give It Another Try ? 😊")
            break

# Start the game with a range up to 10
computer_guess(10)
