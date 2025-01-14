def run(items: list) -> dict:
    unpack_items = {}
    
    for item in items:
        key = item[0]
        value = item[1:]
        unpack_items[key] = value

    return unpack_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
