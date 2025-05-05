def factorial(n):
    if n < 0:
        return None
    
    result = 1
    for value in range(1, n + 1):
        result *= value
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)
