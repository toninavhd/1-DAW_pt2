def run(a: int, b: int) -> float:
    a = abs(a)
    b = abs(b)

    numerator = -a * b**0.5
    denominator = -b * (a**2) * a**0.5
    g_operation = numerator / denominator

    G = round(g_operation, 7)
    return G


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
