def run(text1: str, text2: str) -> int:
    dhamming = 0

    for char in range(len(text1)):
        if text1[char] != text2[char]:
            dhamming += 1
            
    if len(text1) != len(text2):
        dhamming = -1

    return dhamming


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
