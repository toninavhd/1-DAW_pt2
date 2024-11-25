def run(values: list) -> int:
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
    return max_value

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
