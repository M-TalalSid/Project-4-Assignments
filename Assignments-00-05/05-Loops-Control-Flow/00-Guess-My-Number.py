# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

#Solution
import random

def guess_number():
    number = random.randint(0 , 99)
    guess = int(input("Enter A Guess Between 1 To 99 : "))

    while guess != number:
        if guess > number:
            print("Your Guess Is Too High")

        else:
            print("Your Guess Is Too Low ")    

        guess = int(input("Enter A New Guess : ")) 
    # This runs only when the user correctly guesses the number
    print("Congrats ! The Number Was :", number)

if __name__ == "__main__":
    guess_number()