def hyperfactorial(n: int):
    if n == 1:
        return 1

    return (n**n) * hyperfactorial(n-1)
            


    
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(hyperfactorial)
