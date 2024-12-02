def run(A: list, B: list, C: list) -> tuple:
    
    xP = round(((A[0] + B[0] + C[0]) / 3), 4)
    yP = round(((A[1] + B[1] + C[1]) / 3), 4)

    return xP, yP


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
