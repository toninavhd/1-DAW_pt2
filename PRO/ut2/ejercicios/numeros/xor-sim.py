def run(v1: bool, v2: bool) -> bool:

    xor = v1 - v2

    return bool(xor)


if __name__ == '__main__':
    run(False, False)