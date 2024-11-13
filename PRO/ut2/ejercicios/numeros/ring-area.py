def run(z: float) -> float:
    PI = 3.14
    squared_r = z**2
    gray_area = PI * (squared_r + squared_r)
    return gray_area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
