# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.


#Solution

import random

NUM_ROUNDS = 3

def game():
     # Milestone 5: keep track of your score
    SCORE = 0

    print("Welcome To The High-Low Game!")

     # Milestone 4: Play multiple rounds
    for round_num in range(NUM_ROUNDS):
       
        # Milestone 1: Generate the random numbers and print them out
       computer = random.randint(0 , 99)
       user = random.randint(0 , 99)
    #    round_num  = round_num + 1lower
       print( "\nRound" , round_num + 1)
       print("Your Random Number Is" , user)

         # Extension 1: Make sure the player inputs a valid choice (higher or lower)
       user_input = input("Do You Think Your Number Is Higher Or Lower Than The Computer's ?:").lower().strip()

         # Milestone 3: Map out all the ways to win the round
       if user_input == "higher" :
            if user > computer :
                print("✅ You Were Right ! The Computer's Number Was " , computer)
                 #Milestone 5: keep track of  score
                SCORE += 1
            else:
                print("❌ Aww, That's Incorrect. The Computer's Number Was " , computer)

       elif user_input == "lower":
            if user < computer :
                print("✅You Were Right ! The Computer's Number Was " , computer)
                # Milestone 5: keep track of  score
                SCORE += 1
            else:
                print("❌ Aww, That's Incorrect. The Computer's Number Was " , computer)

       else:
          print("⚠️ Invalid Input ! Please Enter 'higher' Or 'lower'.")      

    # Milestone 5: keep track of your score

       print("Your Score Is:" , SCORE)       
  
      # Extension 2: Conditional ending messages based on performance    
    print("Game Over. Your Total Score Is :" , SCORE)    

    if SCORE == 3:
        print("Wow ! You Played Perfectly !")
    elif SCORE == 2:
        print("Good Job, You Played Really Well !")    
    else:
        print("Better Luck Next Time")        
                  
if __name__ == "__main__":
    game()          