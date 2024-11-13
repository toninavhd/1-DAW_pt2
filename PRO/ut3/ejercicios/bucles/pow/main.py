def run(x: int, n: int) -> int:
    counter = 1
    p = 1
    
    while counter <= n:
        counter += 1
        p *= x           
        
    return p


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
