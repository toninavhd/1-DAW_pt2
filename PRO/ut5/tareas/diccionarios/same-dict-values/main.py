def run(items: dict) -> bool:
    values = list(items.values())
    all_same = True
    
    if len(values) == 0:
        all_same = True
    for value in values:
        if value != values[0]:
            all_same = False
            #break

    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
