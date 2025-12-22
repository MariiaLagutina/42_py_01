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


class Flower(Plant):
    """
    Specialized plant type with color and blooming capability.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initializes a flower using the parent Plant constructor.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Displays a blooming message."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Specialized plant type tree with trunk diameter and shade production.
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initializes a tree with a trunk diameter,
        using the parent Plant constructor.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculates and displays the shade area."""
        shade_area = (self.height) * (self.trunk_diameter) * 3.14 / 1000
        print(f"{self.name} provides {shade_area:.1f} square meters of shade")


class Vegetable(Plant):
    """
    Specialized plant type vegeyable with harvest season and nutritional info,
    using the parent Plant constructor.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initializes a vegetable with harvest and nutrition details.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutrition(self) -> None:
        """Displays nutritional information."""
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def ft_plant_types() -> None:
    """
    Demonstrates inheritance by managing a variety of specialized plants.
    """
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 15, "pink")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 450, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    carrot = Vegetable("Carrot", 30, 60, "autumn", "A")

    garden = [rose, tulip, oak, pine, tomato, carrot]

    print("=== Garden Plant Types ===\n")
    for plant in garden:
        if isinstance(plant, Flower):
            print(f"{plant.name} (Flower): {plant.height}cm, {plant.age} "
                  f"days, {plant.color} color")
            plant.bloom()
        elif isinstance(plant, Tree):
            print(f"{plant.name} (Tree): {plant.height}cm, {plant.age} days,"
                  f"{plant.trunk_diameter}cm diameter")
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            print(f"{plant.name} (Vegetable): {plant.height}cm, "
                  f"{plant.age} days, {plant.harvest_season} harvest")
            plant.nutrition()
        print()


if __name__ == "__main__":
    ft_plant_types()
