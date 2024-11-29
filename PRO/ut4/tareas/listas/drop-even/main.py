def run(items: list) -> list:
    clean_list = []
    for item in range(len(items)):
        if item % 2 != 0:
            clean_list.append(items[item])
            filter = clean_list
    return filter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
