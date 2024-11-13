def run():
    range_end = 7

    for left_num in range(range_end):
        row = ''
        for right_num in range(left_num, range_end):
            row += f'{left_num}|{right_num} '
        print(row) 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
