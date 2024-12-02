def run(values: list) -> int:
    if not values:
        target = None
    else:
        first_num = values[0]
        target = None
        for num in values:
            if num != first_num:
                target = num
                break
            else:
                first_num += 1

    return target


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
