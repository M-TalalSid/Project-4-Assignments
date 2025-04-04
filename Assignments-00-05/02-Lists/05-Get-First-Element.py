# Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first

# element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# Solution
def get_first_element(lst):
    """Function To Print The First Element Of The List"""

    print("Here's The First Element Of The List :" , lst[0])

def prompt_list():
    "Prompt The User To Get The Elements f The List"
    lst: list = []
    prompt = input("Please Enter The Element To Add To The List :")
    while prompt != "":
        lst.append(prompt)
        prompt = input("Please Enter The Next Elemnet To Add To The List Or Press Enter To Stop :")
    return lst
    
def main():
    lst = prompt_list()
    get_first_element(lst)

if __name__ == "__main__":
    main()    