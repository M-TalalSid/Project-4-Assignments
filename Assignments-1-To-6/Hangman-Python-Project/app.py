import random

# Dictionary with words and their hints
words_with_hints = {
    "encyclopedia": "📚 A book or resource with detailed information on many topics.",
    "photosynthesis": "🌿 Process plants use to convert sunlight into energy.",
    "architecture": "🏛️ The art and science of designing buildings.",
    "cryptography": "🔐 The study of secure communication techniques.",
    "philosophy": "🤔 The study of fundamental questions about existence and knowledge.",
    "astronomy": "🌌 The study of celestial objects and phenomena.",
    "democracy": "🗳️ A system of government by the whole population.",
    "ecosystem": "🌍 A community of living organisms and their environment.",
    "geography": "🗺️ The study of the Earth's physical features.",
    "history": "📜 The study of past events.",
    "mysticism": "📖 The study of mysticism, a form of spiritualism.",
    "neuroscience": "🧠 The study of the nervous system and brain.",
    "quantum": "⚛️ The study of the smallest particles of matter.",
    "robotics": "🤖 The branch of technology dealing with robots.",
    "sociology": "👥 The study of society and social behavior.",
    "theology": "🕉️ The study of religion.",
    "tactics": "🎯 The art of planning and executing a strategy.",
    "utopia": "🏝️ An imagined place where everything is perfect.",
    "zoology": "🦖 The study of animals.",
    "biochemistry": "🧪 The study of chemical processes within and relating to living organisms.",
    "cybersecurity": "🛡️ The practice of protecting systems from cyber attacks.",
    "entrepreneurship": "💼 The process of starting and running a new business.",
    "philanthropy": "🤝 The desire to promote the welfare of others, often through donations.",
    "vocabulary": "📖 The body of words used in a particular language."
}

def get_hangman_status(attempts):
    """Return hangman status based on remaining attempts using emojis."""
    stages = {
        6: "😁 (All Good !)",
        5: "🙂 (Keep It Up !)",
        4: "😐 (Stay Focused !)",
        3: "😟 (Be Cautious !)",
        2: "😰 (Almost Out !)",
        1: "😨 (Last Chance !)",
        0: "💀 (Game Over !)"
    }
    return stages[attempts]

# Initialize score
wins = 0
losses = 0

print("Welcome To Hangman Game !")
print("You Have 6 Attempts To Guess The Letters In The Word.")
print("Use The Hint To Help You. Good Luck !\n")

play_again = True
while play_again:
    # Start new game
    word, hint = random.choice(list(words_with_hints.items()))
    guessed = []
    attempts = 6
    
    print("\n🎮 New Hangman Game Starts !")
    print(f"💡 Hint: {hint}")
    
    while attempts > 0:
        # Display current state
        display = " ".join([letter if letter in guessed else "_" for letter in word])
        print("\n-------------------")
        print(f"Word: {display}")
        print(f"Status: {get_hangman_status(attempts)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed))}")
        
        guess = input("🔤 Enter A Letter: ").lower()
        
        if len(guess) != 1:
            print("Please Enter Only One Letter.")
            continue
        if not guess.isalpha():
            print("Please Enter A Letter From A To Z.")
            continue
        if guess in guessed:
            print(f"You Already Guessed '{guess}'. Try A Different Letter.")
            continue
        
        guessed.append(guess)
        
        if guess in word:
            print(f"✅ Good Job ! '{guess}' Is In The Word.")
        else:
            attempts -= 1
            print(f"❌ Oops ! '{guess}' Is Not In The Word. Attempts Left: {attempts}")
        
        if all(letter in guessed for letter in word):
            print(f"\n🏆 Congrats ! You Guessed The Word '{word}' Correctly ! 🎉")
            wins += 1
            break
    else:
        print(f"\n💀 Game Over ! The Word Was '{word}'. Better Luck Next Time ! 🔄")
        losses += 1
    
    play_again_input = input("\nDo You Want To Play Again? (Y/N): ").lower()
    if play_again_input != 'y':
        play_again = False

print(f"\nYou Won {wins} Games & Lost {losses} Games. Thanks For Playing !")