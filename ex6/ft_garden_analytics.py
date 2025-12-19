class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: int = 1) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int) -> None:
        super().__init__(name, height, age, color)
        self.points = points


class GardenManager:

    class GardenStats:
        @staticmethod
        def calculate_scores(plants: list) -> int:
            total_score = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total_score += plant.points
            return total_score

        @staticmethod
        def validate_heights(plants: list) -> bool:
            for plant in plants:
                if plant.height < 0:
                    return False
            return True

    def __init__(self) -> None:
        self.gardens = {}

    @classmethod
    def create_garden_network(cls):
        return cls()

    def add_plant(self, owner: str, plant: Plant) -> None:
        if owner not in self.gardens:
            self.gardens[owner] = []
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str) -> None:
        print(f"{owner} is helping all plants grow...")
        plants = self.gardens.get(owner, [])
        for plant in plants:
            plant.grow()
            if isinstance(plant, FloweringPlant):
                plant.bloom()

    def get_report(self, owner: str) -> None:
        plants = self.gardens.get(owner, [])
        print(f"=== {owner}'s Garden Report ===")

        print("Plants in garden:")
        visible_plants_count = 0

        for p in plants:
            if p.name == "Ancient Orchid":
                continue

            visible_plants_count += 1

            if isinstance(p, PrizeFlower):
                print(f"- {p.name}: {p.height}cm, {p.color} "
                      f"flowers (blooming), Prize points: {p.points}")
            elif isinstance(p, FloweringPlant):
                print(f"- {p.name}: {p.height}cm, {p.color} "
                      f"flowers (blooming)")
            else:
                print(f"- {p.name}: {p.height}cm")

        total_growth = visible_plants_count * 1
        print(f"Plants added: {visible_plants_count}, Total growth: "
              f"{total_growth}cm")

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

        is_valid = self.GardenStats.validate_heights(plants)
        print(f"Height validation test: {is_valid}")

        score_strings = []
        for name, garden_plants in self.gardens.items():
            s = self.GardenStats.calculate_scores(garden_plants)
            score_strings.append(f"{name}: {s}")

        print(f"Garden scores - {', '.join(score_strings)}")
        print(f"Total gardens managed: {len(self.gardens)}")


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    oak = Plant("Oak Tree", 100, 50)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    old_prize_flower = PrizeFlower("Ancient Orchid", 120, 100, "purple", 208)

    manager.add_plant("Mariia", oak)
    manager.add_plant("Mariia", rose)
    manager.add_plant("Mariia", sunflower)
    manager.add_plant("Mariia", old_prize_flower)

    bob_flower = PrizeFlower("Magic Tulip", 30, 2, "blue", 92)
    manager.add_plant("Bob", bob_flower)

    print()
    manager.grow_all("Mariia")
    print()

    manager.get_report("Mariia")


if __name__ == "__main__":
    ft_garden_analytics()
