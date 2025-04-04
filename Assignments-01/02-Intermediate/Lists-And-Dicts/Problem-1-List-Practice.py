
# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

#def main(): # Create a list called fruit_list that contains the following fruits: # 'Apple', 'Banana', 'Orange', 'Grape', 'Pineapple', 'Kiwi', 'Peach', 'Cherry', 'Strawberry', 'Blueberry'.

# Print the length of the list.

# Add 'Mango' at the end of the list. 

# Print the updated list.

#Problem 1 solution:

def main():
    fruit_list = ['Apple', 'Banana', 'Orange', 'Grape', 'Pineapple', 'Kiwi', 'Peach', 'Cherry', 'Strawberry', 'Blueberry']
    print(len(fruit_list))
    fruit_list.append("Mango")
    print(fruit_list)

if __name__ == "__main__":
    main()