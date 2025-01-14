def run(d1: dict, d2: dict) -> dict:
    merged = {}
    
    for d in (d1,d2):
        for key, value in d.items():
            merged[key] = value

    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
