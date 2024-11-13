def run(text: str) -> tuple:
    strip_target = 'abcdefghijklmnopqrstuvwxyz-'
    clean_text = text.strip(strip_target)    
    first_digit = int(clean_text[0])
    last_digit = int(clean_text[-1])
    
    return first_digit, last_digit


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
