import time

def get_time_input():
    """Get Valid Time Input From The User In Minutes And Seconds."""
    while True:
        try:
            print("\n" + "="*30)
            print("  ⏳ SIMPLE COUNTDOWN TIMER ⏳  ")
            print("="*30)
            mins = int(input("\nEnter Minutes (0-59): "))
            secs = int(input("Enter Seconds (0-59): "))
            
            if mins < 0 or secs < 0:
                print("❌ Please Enter Non-Negative Numbers!")
                continue
                
            if secs >= 60:
                print("❌ Seconds Must Be Less Than 60!")
                continue
                
            total_seconds = mins * 60 + secs
            if total_seconds == 0:
                print("❌ Timer Cannot Be Zero!")
                continue
                
            return total_seconds
            
        except ValueError:
            print("❌ Please Enter Valid Numbers!")

def display_progress(total, remaining):
    """Display The Countdown Progress With A Bar."""
    progress = (total - remaining) / total
    bar_length = 30
    filled = '▓' * int(bar_length * progress)
    empty = '░' * (bar_length - len(filled))
    return f"[{filled}{empty}] {progress:.0%}"

def countdown(total):
    """Run The Countdown Timer With Visual Feedback."""
    try:
        print("\nStarting Timer! Press Ctrl+C To Stop\n")
        for t in range(total, -1, -1):
            mins, secs = divmod(t, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            progress_bar = display_progress(total, t)
            
            print(f"\r⏳ {timer_display} {progress_bar}", end="", flush=True)
            
            if t > 0:
                time.sleep(1)
                
        print("\n\n" + "="*30)
        print("⏰ TIME'S UP! ⏰")
        print("="*30 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n❌ Timer Stopped By User!")

def main():
    total_seconds = get_time_input()
    countdown(total_seconds)

if __name__ == "__main__":
    main()