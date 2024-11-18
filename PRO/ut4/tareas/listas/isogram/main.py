def run(text: str) -> bool:
    isogram = True
    
    text = text.replace('-','')
    letter_repetitions = []

    for letter in text.lower():
        if letter in letter_repetitions:
            isogram = False
        letter_repetitions.append(letter)
    return isogram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
