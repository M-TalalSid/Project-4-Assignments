# Write a function that takes two numbers and finds the average between the two.

# Solution

def find_average(num1, num2):
    """Function That Takes Two Numbers And Finds The Average"""
    return (num1 + num2) / 2

if __name__ == "__main__":
    try:
        num1 = float(input("Enter The First Number : "))
        num2 = float(input("Enter The Second Number : "))
        avg = find_average(num1, num2)
        print(f"The Average Of {num1} & {num2} Is : {avg}")
    except Exception:
        print("Invalid Input ! Please Enter Numeric Values.")