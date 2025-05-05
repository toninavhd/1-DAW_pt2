def run(morse_path: str, sentence: str) -> str:
    with open(morse_path) as morse_code:
        for line in morse_code:
            morse = dict(letter=line[0].lower(), code=line[1:].strip())

    with open(sentence, 'r') as f:
        for line in f:
            for word in line.lower().strip().split():
                for char in word:
                    if char in morse.keys():
                        morse_sentence = sentence.replace(char, str(morse.values()))
    return morse_sentence


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
