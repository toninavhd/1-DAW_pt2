def run(values: list, power: int) -> int:
    if power < 0 or power >= len(values):
        result = -1
    else:
        result = values[power] ** power
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
