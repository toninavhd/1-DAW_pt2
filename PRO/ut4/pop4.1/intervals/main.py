def run(interval: str) -> list:
    first_symbol = interval[0:1]
    last_symbol = interval[-1:]
    clean_interval = interval[1:-1].split(',')
    first_digit = int(clean_interval[0])
    second_digit = int(clean_interval[1])

    irange = [v for v in range(first_digit, second_digit + 1)]

    if first_symbol == '[' and last_symbol == ']':
        irange = irange
    elif first_symbol == '(' and last_symbol == ']':
        irange = irange[1:]
    elif first_symbol == '[' and last_symbol == ')':
        irange = irange[:-1]
    elif first_symbol == '(' and last_symbol == ')':
        irange = irange[1:-1]

    return irange


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
