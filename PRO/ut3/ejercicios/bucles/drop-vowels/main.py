def run(text: str) -> str:
    VOWELS = 'aeiouAEIOU'
    clean_text = ''

    for char in text:
        if char not in VOWELS:
            clean_text += char
            output = clean_text
    return output


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
