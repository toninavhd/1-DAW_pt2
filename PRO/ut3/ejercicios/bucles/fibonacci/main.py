def run(n: int) -> float:
    num1 = 0
    num2 = 1
    
    for _ in range(2, n + 1):
        next_num = num1 + num2
        num1 = num2
        num2 = next_num
        
    fibo = num2


    return fibo


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
