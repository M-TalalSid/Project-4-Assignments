import random

def generate_password(length):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    special = "&?!@#$%^*"

    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = lower + upper + digits + special

    # Fill remaining length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to randomize placement
    random.shuffle(password)

    return "".join(password)

def get_strength_feedback(length):
    if length >= 12:
        return "Super Strong! 💪"
    elif length >= 8:
        return "Pretty Solid! 👍"
    else:
        return "Good Enough! 😊"

def main():
    print("\n🔐 Hey There! Welcome To Your Password Maker! 🔐")
    print("I’ll Whip Up Some Strong Passwords For You. Let’s Get Started! 😊\n")

    try:
        number = int(input("How Many Passwords Do You Want? "))
        if number <= 0:
            print("❌ Please Enter A Number Greater Than 0. Let’s Try Again!")
            return
        
        password_length = int(input("How Long Should Each Password Be? (4-50): "))
        if password_length < 4:
            print("❌ Oops! Passwords Need To Be At Least 4 Characters Long.")
            return
        if password_length > 50:
            print("❌ Whoa! Max Length Is 50—Let’s Keep It Sensible!")
            password_length = 50  # Cap it at 50

        # Visual Password Length Indicator
        print(f"Length {password_length}: {'*' * password_length}")

        # Generate and display passwords
        print(f"\n📝 Here Are Your {number} Shiny New Passwords:")
        for i in range(number):
            password = generate_password(password_length)
            print(f"{i + 1}. {password}")

        # Password Strength Feedback
        print(f"\n🔒 Strength: {get_strength_feedback(password_length)}")

        # Friendly closing
        print("\n🎉 All Done! Stay Safe With These Passwords! Want More? Just Run Me Again! 😊")

    except ValueError:
        print("❌ Hmm, I Need Numbers, Not Letters! Please Try Again.")

# Start the app
main()