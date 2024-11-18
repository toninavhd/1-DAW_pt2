def run(text: str) -> bool:
    text = text.replace('-','')
    letter_repetitions = []
    isogram = True

    for letter in text:
        if letter in letter_repetitions:
            isogram = False
            break
        letter_repetitions.append(letter)
    return isogram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
