def run(input_path: str, line_no: int) -> str | None:
    line = None
    with open(input_path) as f:
        for num, next_line in enumerate(f, start=1):
            if num == line_no:
                line = next_line.strip()
                break
    return line


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
