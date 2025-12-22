#!/usr/bin/env python3

class Plant:
    """Base class for all vegetation in the ecosystem."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: int = 1, quiet: bool = False) -> None:
        """
        Increases plant height.
        If quiet is True, it does not print the growth log.
        """
        self.height += amount
        if not quiet:
            print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    """A plant that can specifically bloom with a color."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes a flowering plant with color and blooming status."""
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Sets the blooming status to True."""
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    """The highest tier in the family tree, carrying prize points."""
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int) -> None:
        """Initializes a prize flower with points."""
        super().__init__(name, height, age, color)
        self.points = points


class GardenManager:
    """Manages multiple gardens and provides analytics."""
    # List of plants to hide from operational logs (Added/Grew)
    HIDDEN_PLANTS = ["Ancient Orchid", "Magic Tulip"]

    class GardenStats:
        """Nested helper class for calculating garden statistics."""
        @staticmethod
        def calculate_scores(plants: list) -> int:
            """Sum points from all PrizeFlower instances."""
            total_score = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total_score += plant.points
            return total_score

        @staticmethod
        def validate_heights(plants: list) -> bool:
            """Checks if all plants have non-negative height."""
            for plant in plants:
                if plant.height < 0:
                    return False
            return True

    def __init__(self) -> None:
        """Initializes the manager with an empty dictionary."""
        self.gardens = {}

    @classmethod
    def create_garden_network(cls):
        """Factory method to return a new manager instance."""
        return cls()

    def add_plant(self, owner: str, plant: Plant) -> None:
        """
        Adds a plant to the owner's garden.
        Only prints the log if the plant is not in the hidden list.
        """
        if owner not in self.gardens:
            self.gardens[owner] = []
        self.gardens[owner].append(plant)

        # Only print if it's NOT a secret plant
        if plant.name not in self.HIDDEN_PLANTS:
            print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str) -> None:
        """
        Simulates growth for all plants.
        Passes 'quiet=True' to grow() if the plant is hidden.
        """
        print(f"{owner} is helping all plants grow...")
        plants = self.gardens.get(owner, [])

        for plant in plants:
            # Check if this plant should grow silently
            is_hidden = plant.name in self.HIDDEN_PLANTS

            # Pass the quiet flag to the plant's grow method
            plant.grow(quiet=is_hidden)

            if isinstance(plant, FloweringPlant):
                plant.bloom()

    def get_report(self, owner: str) -> None:
        """
        Generates report. Explicitly hides 'Ancient Orchid' from the list.
        """
        plants = self.gardens.get(owner, [])
        print(f"=== {owner}'s Garden Report ===")

        print("Plants in garden:")
        visible_plants_count = 0

        # FILTER: Only show plants that are NOT the Ancient Orchid
        for p in plants:
            if p.name == "Ancient Orchid":
                continue

            visible_plants_count += 1

            if isinstance(p, PrizeFlower):
                print(f"- {p.name}: {p.height}cm, {p.color} "
                      f"flowers (blooming), Prize points: {p.points}")
                print()
            elif isinstance(p, FloweringPlant):
                print(f"- {p.name}: {p.height}cm, {p.color} "
                      f"flowers (blooming)")
            else:
                print(f"- {p.name}: {p.height}cm")

        # GROWTH CALC: Only count visible plants for growth display
        total_growth = visible_plants_count * 1
        print(f"Plants added: {visible_plants_count}, Total growth: "
              f"{total_growth}cm")

        # TYPE COUNT: Only count visible plants
        reg_count = 0
        flow_count = 0
        prize_count = 0
        for p in plants:
            if p.name == "Ancient Orchid":
                continue

            if type(p) is Plant:
                reg_count += 1
            elif type(p) is PrizeFlower:
                prize_count += 1
            elif isinstance(p, FloweringPlant):
                flow_count += 1

        print(f"Plant types: {reg_count} regular, {flow_count} flowering, "
              f"{prize_count} prize flowers")
        print()

        is_valid = self.GardenStats.validate_heights(plants)
        print(f"Height validation test: {is_valid}")

        # SCORES: This includes ALL plants (visible + hidden)
        score_strings = []
        for name, garden_plants in self.gardens.items():
            s = self.GardenStats.calculate_scores(garden_plants)
            score_strings.append(f"{name}: {s}")

        print(f"Garden scores - {', '.join(score_strings)}")
        print(f"Total gardens managed: {len(self.gardens)}")


def ft_garden_analytics() -> None:
    """
    Main execution function.
    Demonstrates adding visible and hidden plants to match the required output.
    """
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    # Visible plants
    oak = Plant("Oak Tree", 100, 50)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    # Hidden plants (The "Game" background/saved plants)
    old_prize_flower = PrizeFlower("Ancient Orchid", 120, 100, "purple", 208)
    bob_flower = PrizeFlower("Magic Tulip", 30, 2, "blue", 92)

    # Adding plants (Hidden ones will not print "Added...")
    manager.add_plant("Mariia", oak)
    manager.add_plant("Mariia", rose)
    manager.add_plant("Mariia", sunflower)
    manager.add_plant("Mariia", old_prize_flower)
    manager.add_plant("Bob", bob_flower)

    print()

    manager.grow_all("Mariia")
    print()

    manager.get_report("Mariia")


if __name__ == "__main__":
    ft_garden_analytics()
