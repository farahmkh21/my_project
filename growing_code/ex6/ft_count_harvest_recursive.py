def ft_count_harvest_recursive(target=None, current=1):
    if target is None:
        day = input("Days until harvest: ")
        target = int(day)
    if current > target:
        print("Harvest time!")
        return
    print("day", current)
    ft_count_harvest_recursive(target, current + 1)
