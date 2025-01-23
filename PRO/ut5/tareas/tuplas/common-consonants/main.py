def run(text1: str, text2: str) -> str:
    clean_target = 'aeiou '
    text1 = text1.lower()
    text2 = text2.lower()

    set1 = set(text1) - set(clean_target)   
    set2 = set(text2) - set(clean_target)
    
    cconst = ''.join(sorted(set1 & set2))

    return cconst


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
