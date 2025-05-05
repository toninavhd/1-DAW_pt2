def run(value1: float, value2: float, vmin: float, vmax: float) -> float:
    rmul = value1 * value2

    if rmul >= vmin:
        rmul = vmax
    elif rmul <= vmax:
        rmul = vmin
    elif vmin <= rmul <= vmax:
        rmul = rmul

    rmul = round(rmul, 2)

    return rmul


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
