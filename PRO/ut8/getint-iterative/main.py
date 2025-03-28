def getint():
    while not :
        try:
            n = int(input('Give me an integer number: '))
        except ValueError:
            print('Not a valid integer. Try it again!')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(getint)
