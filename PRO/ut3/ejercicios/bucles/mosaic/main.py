def run(size: int) -> None:
    LETTER_X = 'X'
    LETTER_D = 'D'
    LETTER_U = 'U'
    x_pos = 1

    for row in range(size):
        u_num = size - x_pos
        d_num = x_pos - 1

        d_line = (LETTER_D + ' ') * d_num
        u_line = (LETTER_U + ' ') * u_num
        x_pos += 1

        print(d_line, LETTER_X + ' ', u_line, sep='')

        
run(5)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
