def run(a: int, b: int) -> int:
    if a < b:
        min = a
    else:
        min = b

    for value in range(1, min + 1):
        if a % value == 0 and b % value == 0:
            gcd_value = value
            
    return gcd_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
