def run(x1: int, x2: int) -> tuple:
    xmin = x1  
    fmin = x1**2 - 6 * x1 + 3

    for value in range(x1, x2 + 1):
        quad_func = value**2 - 6 * value + 3
        if quad_func < fmin:
            fmin = quad_func
            xmin = value

    return xmin, fmin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
