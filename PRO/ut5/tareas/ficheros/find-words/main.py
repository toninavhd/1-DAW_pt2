def run(data_path: str, target_word: str) -> list:
    matches = []
    delimiters = " .,;:()'¡!"
    
    with open(data_path) as f:
        for line_num, line in enumerate(f, start=1):
            words = line.lower().split()

            for word in words:
                clean_word = word.strip(delimiters)
                if clean_word == target_word:
                    column = line.lower().find(word) + 1
                    matches.append((line_num, column))
            
    return matches


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
