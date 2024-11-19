def run(text: str) -> int:
    num_words = 0
    text = text.split()

    for word in text:
        text.count(word)
        num_words += 1
    return num_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
