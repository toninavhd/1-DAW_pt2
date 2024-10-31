def run(limit: int) -> None:
    num = 5
    while num % num == 0 and num < limit:
        print(num)
        num += 5


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
