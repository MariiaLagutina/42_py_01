#!/usr/bin/env python3

class Plant:
    """
    A class used to represent a plant with its physical characteristics.
    """
    def __init__(self, name: str, height: int, age_days: int) -> None:
        """Initializes the plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        """Increases the height of the plant."""
        self.height += 1

    def age(self) -> None:
        """Increases the age of the plant by one day."""
        self.age_days += 1

    def get_info(self) -> str:
        """Returns a string representation of the plant's current status."""
        return f"{self.name}: {self.height}cm, {self.age_days} days old"

    def simulate_day(self) -> None:
        """Simulates a single day of growth and aging."""
        self.grow()
        self.age()

    def simulate_days(self, days: int) -> None:
        """
        Simulates plant growth over a specified number of days.
        """
        for _ in range(days):
            self.simulate_day()


def ft_plant_growth() -> None:
    """
    Main function that simulates a week of growth for a garden
    and prints results.
    """
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)

    garden = [plant_1, plant_2, plant_3]
    original_heights = [p.height for p in garden]

    print("=== Day 1 ===")
    for plant in garden:
        print(plant.get_info())

    for plant in garden:
        plant.simulate_days(6)

    print("=== Day 7 ===")
    for i, plant in enumerate(garden):
        growth = plant.height - original_heights[i]
        print(plant.get_info())
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()

# EXPLANATION OF ENUMERATE:
    #: enumerate()
    # Gives us the index (i) AND the plant object at the same time.
    # We need 'i' to find the matching start height in 'original_heights'.
    #
    # (Manual Index):
    # for i in range(len(garden)):
    #     plant = garden[i]
    #     growth = plant.height - original_heights[i]
    #     ...
