class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = 0
        self._age = 0

        if height >= 0:
            self._height = height
        if age >= 0:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {rose.get_name()}")

    rose.set_height(25)
    rose.set_age(30)

    print()

    rose.set_height(-5)

    print(f"\nCurrent plant: {rose.get_name()} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
