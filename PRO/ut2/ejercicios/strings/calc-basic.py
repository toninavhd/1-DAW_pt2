def run():
    a = int(input('Inserte un número: '))
    b = int(input('Inserte otro número: '))

    sum_result = a + b
    min_result = a - b
    mul_result = a * b
    div_result = a / b

    print(str(a) + '+' + str(b) + '=' + str(sum_result))
    print(str(a) + '-' + str(b) + '=' + str(min_result))
    print(str(a) + '*' + str(b) + '=' + str(mul_result))
    print(str(a) + '/' + str(b) + '=' + str(div_result))
    


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
