def run(values: list, target: int) -> int:
    if len(values) > 0:
        max_diff = abs(target - values[0])
        for value in values[1:]:
            if abs(target - value) > max_diff:
                max_diff = abs(target - value)
    else:
        max_diff = 0
    return max_diff


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
