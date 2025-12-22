#!/usr/bin/env python3

class Plant:
    """
    A class used to represent a plant with its physical characteristics.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        """
        Prints the plant's information in a formatted way.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """
    Main function to manage and display plant registry data.
    """
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant_1.display()
    plant_2.display()
    plant_3.display()


if __name__ == "__main__":
    ft_garden_data()
