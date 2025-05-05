import re


def run(url: str) -> bool:
    regex =  r'https?://\w+(\.\w+)+(/(\w+\.\w+|\w+/?))*'

    return bool(re.fullmatch(regex, url, re.I))
   
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
