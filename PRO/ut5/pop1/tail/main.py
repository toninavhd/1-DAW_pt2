def run(input_path: str, n: int) -> str:
    f = open(input_path)
    all_lines = f.readlines()
    lines = ''.join(all_lines[-n:]).strip()
    return lines


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
