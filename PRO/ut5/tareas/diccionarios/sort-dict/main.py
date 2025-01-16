def run(unsorted_items: dict) -> list[tuple]:
    items = list(unsorted_items.items())

    for item in items:
        sorted_items = (item[0], item[1])
    return sorted_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
