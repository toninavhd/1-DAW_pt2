def run(values: list) -> int:
    if values == []:
        tsum = 0   
    else:
        min_value = min(values)
        max_value = max(values)
        tsum = 0
        for value in values:
            if value != min_value and value != max_value:
                tsum += value
                
    return tsum


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
