def in_range(target: int, first_num: int, last_num: int):
    if target in range(first_num, last_num + 1):
        return True
    else:
        return False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(in_range)
