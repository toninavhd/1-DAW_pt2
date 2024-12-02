def run(formula: list) -> bool:
    case_1 = not (1 in formula and 2 in formula)
    case_2 = not (3 in formula and 4 in formula)
    case_3 = (5 in formula and 6 in formula) or (5 not in formula and 6 not in formula)
    case_4 = 7 in formula or 8 in formula
    
    valid = all([case_1, case_2, case_3, case_4])
    return valid

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
