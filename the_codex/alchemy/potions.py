from elements import create_fire
from elements import create_water

from .elements import create_earth
from .elements import create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed with "
        f"'{create_earth()}' and "
        f"'{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with "
        f"'{create_fire()}' and "
        f"'{create_water()}'"
    )
