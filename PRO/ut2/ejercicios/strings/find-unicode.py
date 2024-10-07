def run(source_char: str, offset: int) -> str:
    unicode_num = ord(source_char)
    target_char = chr(unicode_num + offset)

    return target_char


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
