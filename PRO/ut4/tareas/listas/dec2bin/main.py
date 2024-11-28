def run(n: int) -> str:
    bin_repr = []
    
    if n != 0:
        while n > 0:
            bin_repr.append(str(n % 2))
            n = n // 2
        bin_repr.reverse()
        bin_repr = ''.join(bin_repr)
    else:
        bin_repr = '0'     
           
    return bin_repr


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
