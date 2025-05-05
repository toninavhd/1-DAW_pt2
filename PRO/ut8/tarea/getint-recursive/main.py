def getint():
    try:
        n = int(input('Give me an integer number: '))
        return n
    except ValueError:
        print('Not a valid integer. Try it again!')
        return getint()

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(getint)
