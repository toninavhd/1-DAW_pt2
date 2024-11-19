def run(texts: list) -> list:
    chars = []
    
    for word in texts:
        for char in word:
            chars.append(char)

    return chars


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
