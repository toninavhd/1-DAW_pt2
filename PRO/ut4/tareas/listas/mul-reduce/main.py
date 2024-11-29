def run(numbers: list) -> int:
    rmult = 1
    for number in numbers:
        rmult *= number
    return rmult


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
