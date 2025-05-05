def run(text: str) -> int:
    text_length = len(text)
    initial_vocals = text.lstrip('AEIOUaeiouáéíóúÁÉÍÓÚ')

    nrep = text_length - len(initial_vocals)
    return nrep


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
