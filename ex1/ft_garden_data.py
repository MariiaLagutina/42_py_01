class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


def ft_garden_data() -> None:
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{plant_1.name}: {plant_1.height}cm, {plant_1.days} days old")
    print(f"{plant_2.name}: {plant_2.height}cm, {plant_2.days} days old")
    print(f"{plant_3.name}: {plant_3.height}cm, {plant_3.days} days old")


if __name__ == "__main__":
    ft_garden_data()
