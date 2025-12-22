#!/usr/bin/env python3

def ft_garden_intro() -> None:
    """
    Displays basic information about a plant in the garden.
    This function initializes plant attributes and prints them.
    """
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
# It ensures your script only "acts" when you run it directly,
# but stays quiet when it is being used as a library.
