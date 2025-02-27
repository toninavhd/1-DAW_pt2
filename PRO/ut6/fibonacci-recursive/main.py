def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n    
    
    return fibonacci(n - 1) + fibonacci(n - 2)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(fibonacci)
