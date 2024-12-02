def run(text: str) -> str:
    text = text.lower().split(' ')
    reversing = ' '.join(reversed(text))
    
    return reversing


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
