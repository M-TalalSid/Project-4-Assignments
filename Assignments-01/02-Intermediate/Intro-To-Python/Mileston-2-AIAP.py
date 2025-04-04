
# Milestone #2: Adding in All Planets
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.

#Solution
#Milestone 2:
# Constants 
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Earth": 1.0,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
    "Pluto": 0.063,
    "Moon": 0.165,
    "Sun": 27.9
}

def main():
    earth_weight = float(input("Enter Your Weight On Earth (Kg): "))
    planet = input("Enter A Planet: ").capitalize().strip()  # Capitalize first letter to match dictionary keys
    
    # Check if the planet is Gravity_factor
    if planet in GRAVITY_FACTORS:
        planet_weight = round(earth_weight * GRAVITY_FACTORS[planet], 2)
        print(f"The Equivalent Weight In {planet} Is {planet_weight} Kg")
    else:
        print("\nInvalid Input ! Please Run The Program Again and Enter A Valid Planet Name.")

if __name__ == "__main__":
    main()