def run(items: list, ref_item: object) -> object:
    target_item = None
    
    if ref_item in items:
        ref_index = items.index(ref_item)
        if ref_index < len(items) - 1:
            target_item = items[ref_index + 1]

    return target_item


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
