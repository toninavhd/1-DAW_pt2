def run(words: list) -> dict:
    group_words = {}

    for word in words:
        first_letter = word[0]
        if first_letter not in group_words:
            group_words[first_letter] = []

        group_words[first_letter].append(word)

    return group_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
