# Problem Statement

# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element

# in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# Solution
def get_last_element(lst):
    """Function To Print The Last Element Of The List"""
    print("Here's The Last Element Of The List :" ,lst[len(lst) - 1])
     #or
    # print(list[-1]) 

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
    get_last_element(lst)

if __name__ == "__main__":
    main()