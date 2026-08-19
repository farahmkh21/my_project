def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print(" === Garden Temperature ===\n")

    valid_data = "25"
    print(f"\nInput data is '{valid_data}'")
    try:
        temp = input_temperature(valid_data)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    invalid_data = "abc"
    print(f"\nInput data is '{invalid_data}'")
    try:
        temp = input_temperature(invalid_data)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
