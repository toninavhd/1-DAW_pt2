def extract_evens(values: list[int]) -> list:
    result = []
    for value in values:
        if value % 2 == 0:
            result.append(value)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(extract_evens)
