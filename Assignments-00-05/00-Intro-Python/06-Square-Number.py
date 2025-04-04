# Problem Statement

# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics): Type a number to see its square: 4

# 4.0 squared is 16.0

# Solution

def main():
    
    #prompt the user to enter a number
    number  =  input("Enter A Number To See Its Square :")

    #convert the input to a float
    number = float(number)

    print(f"{number} Squared Is {number ** 2}")

if __name__ == "__main__":
    main()