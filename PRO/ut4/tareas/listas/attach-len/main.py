def run(text: str) -> list:
    words = text.split()
    words_length = []

    for word in words:
        word_len = f'{word}:{len(word)}'
        words_length.append(word_len)
        
    return words_length


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
