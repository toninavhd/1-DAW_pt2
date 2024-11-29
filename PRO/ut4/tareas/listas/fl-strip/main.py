def run(numbers: str) -> str:
    clean_numbers = numbers.split(',')

    strip_numbers = clean_numbers[1:-1]
    strip_numbers = ' '.join(strip_numbers)

    return strip_numbers


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
