def run(values: list) -> list:
    odds = []
    for value in values:
        if value % 2 != 0 and value not in odds:
            odds.append(value)

    return odds


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
