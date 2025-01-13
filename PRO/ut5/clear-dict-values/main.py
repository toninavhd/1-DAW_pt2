def run(items: dict) -> dict:
    citems = {}
    
    for key, value in items.items():
        value = []
        citems[key] = value

    return citems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
