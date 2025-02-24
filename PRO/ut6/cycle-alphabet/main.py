def cycle_alphabet(limit:int) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET_SIZE = len(ALPHABET)
    f_limit = limit % ALPHABET_SIZE

    return ALPHABET[:f_limit]



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cycle_alphabet)
