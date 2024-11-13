def run(text1: str, text2: str) -> str:
    cartesian = ''
    
    for char in text1:
        for letter in text2:
            sum_chars = char + letter
            cartesian += sum_chars

    return cartesian


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
