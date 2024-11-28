def run(items: list) -> bool:
    all_same = True

    for item in items:
        if item != items[1]:
            all_same = False
            
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
