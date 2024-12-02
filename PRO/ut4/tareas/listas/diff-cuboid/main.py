def run(cuboid1: list, cuboid2: list) -> float:
    vol_1 = 1
    vol_2 = 1

    for num in cuboid1:
        vol_1 *= num
    for num in cuboid2:
        vol_2 *= num

    vol_diff = abs(vol_1-vol_2)

    return vol_diff


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
