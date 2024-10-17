def run(symbol: str) -> str:
    coma_pos = symbol.index(',')
    coeficent = int(symbol[:coma_pos])
    exponent = int(symbol[coma_pos:])
    new_expo = exponent + 1
    new_coef = coeficent // new_expo

    integral = f'{new_coef}x^{new_expo}'

    return integral


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
