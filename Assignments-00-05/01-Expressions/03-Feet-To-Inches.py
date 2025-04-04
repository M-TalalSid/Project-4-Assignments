# Problem Statement

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Solution

def main():
    """Program To Convert Feet Into Inches"""

    feet : float = float(input("Enter The Value In Feet"))
    
    #convert the feet into inches  e.g 1 foot = 12 inches
    inches = feet * 12

    print(f"{feet} feet = {inches} inches")

if __name__ == "__main__":
    main()