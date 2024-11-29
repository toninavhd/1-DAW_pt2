def run(numbers: list) -> int:
    result = 0
    for number in numbers:
        if number > 0:
            result += number
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
