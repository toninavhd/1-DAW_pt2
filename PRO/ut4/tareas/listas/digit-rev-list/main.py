def run(number: int) -> list:
    
    rev_digits = [int(num) for num in reversed(str(number))]
    return rev_digits


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
