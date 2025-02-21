def count_vowels(text: str):
    VOWELS = 'aeiouáéíóú'
    counter = 0
    for char in text.lower():
        if char in VOWELS:
            counter += 1
            return counter
    return


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(count_vowels)
