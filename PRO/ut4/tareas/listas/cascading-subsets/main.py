def run(values: list, size: int) -> list:
    cascading = []

    for value in range(len(values) - size + 1): 
        subset = values[value:value + size] 
        cascading.append(subset)

    return cascading


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
