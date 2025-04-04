# Problem Statement
# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing 
# anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain
# times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may 
# be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to.
# Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. 
# I am capable of doing anything I put my mind to. That's right! :)

# Note that you can call input() with no prompt and it will still wait for a user to type something!

# Solution 

affirmation_sentence = """I Am Capable Of Doing Anything I Put My Mind To."""

def main():
    print("Please Type The Following Affirmation: " + affirmation_sentence)
    # prompt the user
    user = input()
    while user != affirmation_sentence:
        print("Hmmm That Was Not The Affirmation")

        print("Please Type The Following Affirmation: " + affirmation_sentence)

        user = input()
    print("I Am Capable Of Doing Anything I Put My Mind To. That's Right !")    
        
if __name__ == "__main__":
    main()    