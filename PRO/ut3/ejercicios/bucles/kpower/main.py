def run(n: int) -> tuple:
    sum_num = 0
    right_side = 0

    for num in range(1, n + 1):
        sum_num += num
        right_side += num ** 3
    
    left_side = sum_num ** 2
                 
    return left_side, right_side


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
