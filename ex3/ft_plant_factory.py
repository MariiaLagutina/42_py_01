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


def ft_plant_factory() -> None:
    """
    Creates multiple plants from a data set and displays their information.
    """
    orders = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Peony", "height": 20, "age": 5},
        {"name": "Cactus", "height": 9, "age": 300},
        {"name": "Sunflower", "height": 210, "age": 65},
        {"name": "Orchid", "height": 55, "age": 120}
    ]

    print("=== Plant Factory Output ===")
    for order in orders:
        plant = Plant(**order)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print(f"\nTotal plants created: {len(orders)}")


if __name__ == "__main__":
    ft_plant_factory()
