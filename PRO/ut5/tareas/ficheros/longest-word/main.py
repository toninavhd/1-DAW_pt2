def run(input_path: str) -> str:
    SEPARATOR = ' \n,.;:()'
    longest_word = ''

    with open(input_path) as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) >= len(longest_word):
                    longest_word = word.strip(SEPARATOR)
    return longest_word


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
