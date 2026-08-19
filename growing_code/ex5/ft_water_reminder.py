def ft_water_reminder():
    j = input("Days since last watering:")
    i = int(j)
    if i > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
