def run(text: str) -> int:
    vowel_counter = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    metric = int(vowel_counter * len(text))
    return metric


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
