def run(n: int) -> list:
    dnums = [num for num in range(1,n + 1)]
    dnums = list(reversed(dnums))
    return dnums


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
