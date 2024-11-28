def run(values: list) -> int:
    min_value = max(values)
    for value in values:
        if value < min_value:
            min_value = value
    return min_value

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
