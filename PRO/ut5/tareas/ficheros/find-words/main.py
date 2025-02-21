def run(data_path: str, target_word: str) -> list:
    DELIMITERS = " .,;:()'¡!"
    matches = []
    target_word = target_word.lower()

    with open(data_path) as f:
        for line_num, line in enumerate(f, start=1):
            words = line.split()
            index_offset = 0
            for word in words:
                clean_word = word.strip(DELIMITERS)
                if clean_word == target_word:
                    column = line.index(word, index_offset) + 1
                    matches.append((line_num, column))
                index_offset += len(word) + 1

    return matches


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
