def run(input_path: str) -> str:
    longest_word = ''
    separator = ' \n,.;:()'

    with open(input_path) as f:
        for line in f:
            words = line.split()
            for word in words:             
                if len(word) >= len(longest_word):
                    longest_word = word.strip(separator)
    return longest_word


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
