def ft_plant_age():
    ag = input("Enter plant age in days:")
    age = int(ag)
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
