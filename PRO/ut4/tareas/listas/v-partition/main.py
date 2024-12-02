def run(values: list, ref_value: int) -> list:
    max_values = [value for value in values if value >= ref_value]
    min_values = [value for value in values if value < ref_value]
    
    vpartition = [min_values, max_values]
    return vpartition


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
