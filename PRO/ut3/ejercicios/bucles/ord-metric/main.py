def run(text: str) -> float:
    counter = 0
    text_len = len(text)

    for char in text:
        counter += ord(char)
        tmetric = round((counter / text_len), 2)

    return tmetric


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
