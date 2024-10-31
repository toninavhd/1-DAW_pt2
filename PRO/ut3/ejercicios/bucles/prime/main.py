def run(n: int) -> bool:
    is_prime = True

    for value in range(2, n):
        if n % value == 0:
            is_prime = False

    return is_prime


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
