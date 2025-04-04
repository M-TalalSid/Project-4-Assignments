# Problem Statement

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words !

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually

# filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning 

# of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

# Solution

def main():
    SENTENCE_START = "Code In Place Is Fun. I Learned To Program And Used Python To Make My"

# Taking user inputs

    adjective = input("Please Type An Adjective And Press Enter : ")
    noun = input("Please Type A Noun and Press Enter : ")
    verb = input("Please Type A Verb And Press Enter : ")

# Printing the final sentence

    story = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    print(story)
    
if __name__ == "__main__":
    main()