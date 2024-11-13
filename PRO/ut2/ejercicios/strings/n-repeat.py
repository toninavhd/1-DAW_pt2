def run(n: int) -> int:
    n_calc = str(n + n * 11 + n * 111)
    result = int(n_calc)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
