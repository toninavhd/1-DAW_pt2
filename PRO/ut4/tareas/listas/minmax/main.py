def run(values: list) -> tuple:
    max_value = values[0]
    min_value = values[-1]

    for value in values:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value

    return min_value, max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
