# Problem Statement
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

# Here is a joke for you! Panaversity GPT - Alexandra is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Alexandra returns with 13 liters of milk. The programmer asks why and Alexandra replies: 'because they had eggs'

# If the user enters anything else we print out:

# Sorry I only tell jokes

# You should use the three constants:

# PROMPT JOKE SORRY

# which contain the strings for the prompt asked to the user, the joke to print out if the user enters Joke and the sorry message if the user enters anything else.

# Your program will need to use an if statement which checks if the user input is Joke:

# if user_input == "Joke":

# Recall that == is a comparison which tests if two values are equal to one another.

# Here is a full run of the program (user input is in blue):

# What do you want? Joke Here is a joke for you! Panaversity GPT - Alexandra is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Alexandra returns with 13 liters of milk. The programmer asks why and Alexandra replies: 'because they had eggs'


#Solution:
# Constants (as per the problem statement)
PROMPT = "What Do You Want ? "
JOKE = ("Here Is A Joke For You ! Alexandra Is Heading Out To The Grocery Store. "
        "A Programmer Tells Her : Get A Liter Of Milk, and If They Have Eggs, Get 12. "
        "Alexandra Returns With 13 Liters Of Milk. The Programmer Asks Why and Alexandra Replies : 'Because They Had Eggs'")
SORRY = "Sorry I Only Tell Jokes."

# Function to handle user input
def joke_bot(prompt_user: str) -> str:
    if prompt_user.lower().strip() == "joke":
        return JOKE
    else:
        return SORRY  


def main():
    user_input = input(PROMPT)  
    print(joke_bot(user_input))

if __name__ == "__main__":
    main()
