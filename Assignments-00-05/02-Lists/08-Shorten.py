# Problem Statement

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, 

# and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than

# MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes 

# it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but 

# feel free to change it around to test your program.

#Solution
def shorten(lst):
    """Function To Remove Elements From The End Of The List Until It Is MAX_LENGTH Items Long"""
    MAX_LENGTH = 3
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(f"Removing {removed_element} From The List")

def prompt_list():
    """Prompt The User To Enter Elements For The List"""
    lst = []
    elem = input("Enter An Element To Add To The List (Press Enter To Stop) : ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter The Next Element (Press Enter To Stop) : ")
    return lst        

def main():
    lst = prompt_list()
    shorten(lst)
    #print the final list after shorten
    print(f"Final List After Shortening : {lst}")  

#function to run the code
if __name__ == "__main__":
    main()