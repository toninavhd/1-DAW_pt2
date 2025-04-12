import re


def run(expression: str) -> int | float:
    regexp = r'\s*([+\-*/])\s*'
    op = re.split(regexp, expression)
    n_1 = int(op[0])
    n_2 = int(op[2])
    operator = op[1]

    if operator == '+':
        return n_1 + n_2
    elif operator == '-':
        return n_1 - n_2
    elif operator == '*':
        return n_1 * n_2
    elif operator == '/':
        return n_1 / n_2

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
