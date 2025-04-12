import re


def run(number: str) -> bool:
    regxp = '((\d*|-?\d+)_?\.\d*(_?\d+)*|\d+[Ee]\d+)'
    return bool(re.fullmatch(regxp,number))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
