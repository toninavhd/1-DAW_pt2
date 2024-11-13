def run(text: str, target_word: str, replace_word: str) -> str:
    word_index = text.find(target_word)
    text_part = text[:word_index:]
    word_lenght = word_index + len(target_word)
    text_part2 = text[word_lenght:]

    mtext = text_part + replace_word + text_part2
    return mtext


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
