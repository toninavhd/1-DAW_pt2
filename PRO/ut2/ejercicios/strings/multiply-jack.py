def run(n: int) -> int:
    digit_count= len(str(n).strip('-'))
    result = int(n * (5 ** digit_count))
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
