def cycle_alphabet(num_chars: int):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET_SIZE = len(ALPHABET)
    
    for char in range(num_chars):
        yield ALPHABET[char % ALPHABET_SIZE]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cycle_alphabet)
