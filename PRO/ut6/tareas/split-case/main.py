def split_case(words):
    upper_words = [word for word in words if word == word.upper()]
    lower_words = [word for word in words if word == word.lower()]
    return lower_words, upper_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(split_case)
