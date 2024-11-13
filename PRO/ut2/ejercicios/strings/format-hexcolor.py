def run(intcolor: int) -> str:
    hex_value = hex(intcolor)[2:].upper()
    hexcolor = f'#{hex_value:0>6s}'
    return hexcolor


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
