def bsort(values: list):
    limit_range = len(values)
    for num in range(limit_range):
        for j in range(0, limit_range-num-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    return values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(bsort)
