def run(number: int) -> int:
    num_divisors = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            num_divisors += 1

    return num_divisors


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
