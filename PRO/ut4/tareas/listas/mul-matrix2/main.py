def run(A: list, B: list) -> list:
    pos_1 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    pos_2 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    pos_3 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    pos_4 = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    P = [[pos_1, pos_2], [pos_3, pos_4]]
    return P


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
