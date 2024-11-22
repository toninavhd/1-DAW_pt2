def run(nums_dups: list) -> list:
    nums_unique = []

    for value in nums_dups:
        if value not in nums_unique:
            nums_unique.append(value)

    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
