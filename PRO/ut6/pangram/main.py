def is_pangram(text: str) -> bool:
    VOWELS = 'aeiou'
    NUM_VOWELS = 5
    counter = 0
    clean_text = set(text.replace(' ', '').lower())

    pangram = False
    for char in clean_text:
        if char in VOWELS:
            counter += 1
            if counter == NUM_VOWELS:
                pangram = True

    return pangram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_pangram)
