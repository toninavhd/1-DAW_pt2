def run(number: int) -> str:
    nbin = bin(number)[2:]
    return nbin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
