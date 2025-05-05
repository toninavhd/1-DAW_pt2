def get_max(items: list) -> int:
    if len(items) == 1:
        return items[0]
    else:
        return items[0] if items[0] > get_max(items[1:]) else get_max(items[1:])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(get_max)
