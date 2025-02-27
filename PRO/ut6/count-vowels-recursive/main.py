def count_vowels(text: str):
    VOWELS = 'aeiouáéíóú'
    if not text:
        return 0
    
    first_char = text[0].lower()
    if first_char in VOWELS:
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(count_vowels)
