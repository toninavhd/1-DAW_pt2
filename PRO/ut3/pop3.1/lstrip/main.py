def run(text: str, strip_chars: str) -> str:
    stext = ''

    for char in text:
        if char not in strip_chars:
            while strip_chars != char:
                stext += char
                break

    return stext


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
