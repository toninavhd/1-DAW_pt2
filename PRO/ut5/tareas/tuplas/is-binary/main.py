def run(number: str) -> bool:
    binary = True

    for n in number:
        if n not in '01':
            binary = False
    return binary

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
