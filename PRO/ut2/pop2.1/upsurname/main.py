def run(fullname: str) -> int:
    cut_target = fullname.index(',')
    name = len(fullname[cut_target + 1 :])
    surname = fullname[:cut_target]
    upper_name = surname.isupper()

    fmetric = name + upper_name
    return fmetric


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
