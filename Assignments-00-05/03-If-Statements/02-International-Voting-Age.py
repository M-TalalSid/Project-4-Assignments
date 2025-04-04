# Problem Statement

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

#Solution
def main():
    """This Function Asks The User For Their Age And Lets Them Know If They Can Or Can't 
    Vote In The Following Three Fictional Countries."""

    age = int(input("How Old Are You ? ")) 

    if age >= 16:
        print("You Can vote in Peturksbouipo where the voting Age Is 16.")

    else:
        print("You Cannot vote in Peturksbouipo where the voting Age Is 16.")

    if age >= 25:
        print("You Can Vote In Stanlau Where The Voting Age Is 25.")

    else:
        print("You Cannot Vote In Stanlau Where The Voting Age Is 25.")

    if age >= 48:
        print("You Can Vote In Mayengua Where The Voting Age Is 48.")    

    else:
        print("You Cannot Vote In Mayengua Where The Voting Age Is 48.")   

if __name__ == "__main__":
    main()