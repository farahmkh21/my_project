from typing import Any


def garden_operations(operation_number: int) -> Any:
    if operation_number == 0:
        return int("abc")

    elif operation_number == 1:
        return 1 / 0

    elif operation_number == 2:
        return open(
            "/non/existent/file",
            "r"
        )

    elif operation_number == 3:
        return "string" + 42

    return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")

        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as e:
            error_name = type(e).__name__
            print(f"Caught {error_name}: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
