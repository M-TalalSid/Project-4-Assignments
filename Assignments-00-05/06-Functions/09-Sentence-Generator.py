# Problem Statement
# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech,
#  place the word into one of three sentence templates (or one from your imagination!):

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"

# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"

# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.

# Here's a sample run of the program (user input is in blue):

# Please type a noun, verb, or adjective: groovy Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: 2 Looking out my window, the sky is big and groovy!

#sloution

def sentence(word , part_of_speech):
  
    if part_of_speech == 0:
        print(f"I am Excited To Add This {word} To My Vast Collection Of Them !")

    elif part_of_speech == 1:
        print(f"It's So Nice Outside Today It Makes Me Want To {word} !")

    elif part_of_speech == 2:
        print(f"Looking Out My Window, The Sky Is Big And {word} !")

    else:
        print("Part Of Speech Must Be 0, 1, Or 2 ! Can't Make A Sentence.")

def main():
    word :  str = input("Please Type A Noun, Verb, Or Adjective : ")
    print("Is This A Noun, Verb, Or Adjective ?")
    part_of_speech = int(input("Type 0 For Noun, 1 For Verb, 2 For Adjective : "))
   
    sentence(word, part_of_speech)

if __name__ == '__main__':
    main()