import re


def run(email: str) -> bool:
    regex = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,8}$'
    return bool(re.fullmatch(regex, email, re.I))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
