def run():
    while True:
        name = input('¿Su nombre? ')
        if name == name.title():
            print(name)
            break
        else:
            print('Error. Debe escribirlo correctamente')



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
