def run(marks: dict) -> tuple:
    passed = {name.upper(): mark for name, mark in marks.items() if mark >= 5}
    failed = {name.lower(): mark for name, mark in marks.items() if mark < 5}
    return passed, failed


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
