# Problem Statement

# Write a program which continuously asks the user to enter values which are added one by one into a list. 

# When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

# Solution
def get_list(lst):
    """Function To Print The Entire Element Of The List"""
    print("Here's The List :" , lst) 

def prompt_list():
    """Prompt The User To Enter Elements For The List"""
    lst = []
    prompt = input("Enter An Element To Add To The List (Press Enter To Stop) : ")
    while prompt != "":
        lst.append(prompt)
        prompt = input("Enter The Next Element (Press Enter To Stop) : ")
    return lst

def main():
    lst = prompt_list()
    get_list(lst)

if __name__ == "__main__":
    main()