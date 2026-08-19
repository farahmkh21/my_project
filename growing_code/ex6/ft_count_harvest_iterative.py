def ft_count_harvest_iterative():
    days = input("Days until harvest: ")
    day = int(days)

    for i in range(1, day + 1):
        print("Day", i)
    print("Harvest time!")
