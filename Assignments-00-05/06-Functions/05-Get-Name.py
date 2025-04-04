# Problem Statement
# Fill out the get_name() function to return your name as a string! We've written a main() function for you 
# which calls your function to retrieve your name and then prints it in a greeting.

# Here's a sample run of the program where the name we've decided to return is Alexandra (the autograder expects
# the returned name to be Alexandra):

# Howdy Alexandra ! 🤠

def get_name(name):
    return name

def main():

    print("Howdy" , get_name("Alexandra") , "! 🤠")

if __name__ == "__main__":
    main()