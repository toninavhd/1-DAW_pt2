def is_palindrome(text: str) -> bool:
    clean_text = text.replace(' ', '').lower()

    return clean_text == clean_text[::-1]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_palindrome)
