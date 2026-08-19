class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown watering error") -> None:
        GardenError.__init__(self, message)


def simulate_garden(scenario: int) -> None:
    if scenario == 0:
        raise PlantError("The tomato plant is wilting!")
    elif scenario == 1:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        simulate_garden(0)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        simulate_garden(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for i in range(2):
        try:
            simulate_garden(i)
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
