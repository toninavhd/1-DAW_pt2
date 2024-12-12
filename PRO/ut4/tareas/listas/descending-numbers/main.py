def run(n: int) -> list:
    dnums = [num for num in range(n, 0,- 1)]
    return dnums


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
