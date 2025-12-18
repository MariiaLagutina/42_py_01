class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def grow_older(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"
    
    def simulate_day(self) -> None:
        self.grow()
        self.grow_older()

    def simulate_days(self, days: int) -> None:
        for _ in range(days):
            self.simulate_day()


def ft_plant_growth() -> None:
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
