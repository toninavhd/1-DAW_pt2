def run(words: list) -> str:
    dword = ''
    letter_count = 0

    for word in words:
        unique_letters = set(word)
        word_length = len(unique_letters)

        if word_length > letter_count:
            dword = word
            letter_count = word_length

    return dword


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
