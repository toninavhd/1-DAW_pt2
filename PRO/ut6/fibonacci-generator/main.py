def fibonacci(n: int):
    result = 0
    for values in range(n):
        result += values
        yield result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(fibonacci)
