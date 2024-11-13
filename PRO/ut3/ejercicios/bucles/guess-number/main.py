def run(target_number: int) -> None:
    tries = 0
    
    while True:
        num = int(input('Introduzca número: '))
        tries += 1
        if num < target_number:
            print('Mayor')
        elif num > target_number:
            print('Menor')
        else:
            break
    print(f'Enhorabuena has encontrado el número en {tries} intentos')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
