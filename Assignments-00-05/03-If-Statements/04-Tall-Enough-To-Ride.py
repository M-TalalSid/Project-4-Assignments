# Problem Statement

# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

#Solution

def main():
    """This Function Asks The User How Tall They Are And Prints Whether Or Not They're Taller Than 
    A Pre-Specified Minimum Height."""
    while True:
        height = int(input("How Tall Are You ? "))
        if height == "":
            break
        if int(height) >= 50:
            print("You're Tall Enough To Ride !")
        else:
            print("You're Not Tall Enough To Ride, But Maybe Next Year !")

if __name__ == "__main__":
    main()            