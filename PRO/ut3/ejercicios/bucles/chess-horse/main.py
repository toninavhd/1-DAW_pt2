def run(target_x: int, target_y: int) -> int:
    x = 0
    y = 0
    movements = 0

    while x < target_x or y < target_y:
        if movements % 2 == 0:
            x += 1
            y += 2
        else:
            y += 1
            x += 2
        movements += 1
    if target_x != x or target_x != y:
        movements = -1       

    return movements


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
