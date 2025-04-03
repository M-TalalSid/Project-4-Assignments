import random

def play_game(total_user_wins, total_computer_wins):
    print("\n🎉 Hey There! Welcome To Rock, Paper, Scissors! 🎉")
    print("It’s A Best-Of-3 Showdown. Let’s See Who’s The Champ! 😊\n")

    user_score = 0
    computer_score = 0
    choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}

    while user_score < 2 and computer_score < 2:
        # Visual Scoreboard with stars
        print(f"📊 Score: You {'★' * user_score}{'☆' * (2 - user_score)} - Me {'★' * computer_score}{'☆' * (2 - computer_score)}")
        user = input("Pick One: 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
        
        if user not in choices:
            print("Oops, that’s not a valid choice! Try 'r', 'p', or 's'. 😅")
            continue
        
        computer = random.choice(["r", "p", "s"])
        print(f"🖥️ I Chose: {choices[computer]}")

        if user == computer:
            print(f"🤝 We Both Picked {choices[user]}! It’s A tie!")
        elif is_win(user, computer):
            print(f"✅ Nice One! Your {choices[user]} Beats My {choices[computer]}!")
            user_score += 1
        else:
            print(f"❌ Oof, My {choices[computer]} Beats Your {choices[user]}!")
            computer_score += 1

        # Tiebreaker announcement
        if user_score == 1 and computer_score == 1 and (user_score + computer_score) == 2:
            print("\n⚡ It’s 1-1! Time For The Ultimate TieBreaker Round! ⚡")

    # Final result for this game
    print(f"\n🏆 Game Over! You {'★' * user_score}{'☆' * (2 - user_score)} - Me {'★' * computer_score}{'☆' * (2 - computer_score)}")
    if user_score == 2:
        print("🎉 Woo-Hoo! You’re The Champ This Time! Great Job! 😊")
        total_user_wins += 1
    else:
        print("😢 I Got This One! Better Luck Next Time! 😉")
        total_computer_wins += 1

    # Show total wins across games
    print(f"🌟 All-Time Wins: You {total_user_wins} - Me {total_computer_wins}")

    # Play again option
    play_again = input("\nWant To Play Again? Type 'y' For Yes Or 'n' For No: ").lower()
    if play_again == 'y':
        return play_game(total_user_wins, total_computer_wins)  # Recursive call with updated totals
    else:
        print("Thanks For Playing! See You Next Time! 👋")
        return total_user_wins, total_computer_wins

def is_win(player, opponent):
    return (player == "r" and opponent == "s") or \
           (player == "s" and opponent == "p") or \
           (player == "p" and opponent == "r")

# Start the game with initial total wins at 0
total_user_wins = 0
total_computer_wins = 0
total_user_wins, total_computer_wins = play_game(total_user_wins, total_computer_wins)