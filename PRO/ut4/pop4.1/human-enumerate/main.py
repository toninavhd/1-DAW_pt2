def run(items: str) -> str:
    splited_items = items.split(':')
    if len(splited_items) > 1:
        last_item = splited_items[-1]
        enum_items = ', '.join(splited_items[:-1]) + ' and ' + last_item
    else:
        enum_items = items

    return enum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
