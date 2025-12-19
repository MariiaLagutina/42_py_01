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
    def __init__(self, name: str, height: int, age: int, color: str, points: int) -> None:
        super().__init__(name, height, age, color)
        self.points = points

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

class GardenManager:
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
        for p in plants:
            if isinstance(p, PrizeFlower):
                print(f"{p.name}: {p.height}cm, {p.color} flowers (blooming), ", end="")
                print(f"Prize points: {p.points}")
            elif isinstance(p, FloweringPlant):
                print(f"{p.name}: {p.height}cm, {p.color} flowers (blooming)")
            else:
                print(f"{p.name}: {p.height}cm")
        
        total_growth = len(plants) * 1 
        print(f"Plants added: {len(plants)}, Total growth: {total_growth}cm")
        
        reg_count = sum(1 for p in plants if type(p) is Plant)
        flow_count = sum(1 for p in plants if isinstance(p, FloweringPlant) 
                         and not isinstance(p, PrizeFlower))
        prize_count = sum(1 for p in plants if isinstance(p, PrizeFlower))

        
        print(f"Plant types: {reg_count} regular, {flow_count} flowering, {prize_count} prize flowers")
        
        is_valid = GardenStats.validate_heights(plants)
        score = GardenStats.calculate_scores(plants)
        
        print(f"Height validation test: {is_valid}")
        print(f"Garden scores {owner}: {score}")
        print(f"Total gardens managed: {len(self.gardens)}")



def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===")
    
    manager = GardenManager.create_garden_network()
    
    oak = Plant("Oak Tree", 100, 50)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    
    manager.add_plant("Mariia", oak)
    manager.add_plant("Mariia", rose)
    manager.add_plant("Mariia", sunflower)
    
    manager.gardens["Kate"] = [] 
    
    print()
    manager.grow_all("Mariia")
    print()
    
    manager.get_report("Mariia")


if __name__ == "__main__":
    ft_garden_analytics()
    