import re


def run(text: str) -> list[str]:
    regexp = r'\W([aeiouáéíóú][a-záéíóú]*)'
    return re.findall(regexp,text, re.I)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
