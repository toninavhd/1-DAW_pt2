def run(values1: list, values2: list) -> list:
    unsorted_values = values1.extend(values2)
    for value in unsorted_values:
        if value > unsorted_values[0]:
            merged += value
    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
