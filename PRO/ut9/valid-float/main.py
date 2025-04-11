import re


def run(number: str) -> bool:
    regxp = '\d*\.\d+'
    return bool(re.findall(regxp,number))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
