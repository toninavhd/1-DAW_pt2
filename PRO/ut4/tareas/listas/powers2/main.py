def run(n: int) -> list:
    powers2 = []
    base = 2

    for exponent in range (0, n + 1):
        power = base ** exponent
        powers2.append(power)
    return powers2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
