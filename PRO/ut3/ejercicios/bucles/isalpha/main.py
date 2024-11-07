def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    
    isalpha = True
    for letter in text.lower():
        if letter not in ALPHABET:
            isalpha = False

    return isalpha


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
