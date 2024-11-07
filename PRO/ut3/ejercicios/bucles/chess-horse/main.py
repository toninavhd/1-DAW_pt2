def run(target_x: int, target_y: int) -> int:
    x = 1
    y = 1
    movements = 0

    while x < target_x or y < target_y:
        if x < target_x:
            x += 2
            y += 1
        elif y < target_y:
            y += 2
            x += 1
        movements += 1
        if target_x < x and target_x < y:
            movements = -1       

    return movements


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
