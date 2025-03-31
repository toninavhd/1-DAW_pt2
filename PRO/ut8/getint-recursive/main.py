def getint():
    is_integer = False
    while not is_integer:
        try:
            n = int(input('Give me an integer number: '))
            is_integer = True
        except ValueError:
            print('Not a valid integer. Try it again!')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(getint)
