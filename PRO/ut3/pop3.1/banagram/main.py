def run(word1: str, word2: str) -> bool:
    is_banagram = True

    for char in word1.lower():
        if char not in word2.lower():
            is_banagram = False

    return is_banagram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
