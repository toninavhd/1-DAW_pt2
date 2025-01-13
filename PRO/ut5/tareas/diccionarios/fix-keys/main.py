def run(items: dict) -> dict:
    fitems = {}

    for key, value in items.items():
        fixed_keys = key.replace(' ','')
        fitems[fixed_keys] = value

    return fitems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
