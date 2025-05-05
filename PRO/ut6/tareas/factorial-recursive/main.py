def factorial(n: int):
    if n == 0:
        return 1
    elif n < 0:
        return None
    else:
        return n * factorial(n - 1)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)
