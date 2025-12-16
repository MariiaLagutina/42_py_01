class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    orders = [
        {"name": "Rose", "h": 25, "d": 30},
        {"name": "Peony", "h": 20, "d": 5},
        {"name": "Cactus", "h": 9, "d": 300},
        {"name": "Sunflower", "h": 210, "d": 65},
        {"name": "Orchid", "h": 55, "d": 120}
    ]

    print("=== Plant Factory Output ===")
    count = 0

    for order in orders:
        p_name = order["name"]
        p_height = order["h"]
        p_age = order["d"]

        new_plant = Plant(p_name, p_height, p_age)

        print(f"Created: {new_plant.name} ", end="")
        print(f"({new_plant.height}cm, {new_plant.age} days)")

        count += 1

    print()
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
