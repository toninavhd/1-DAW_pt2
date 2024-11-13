def run(start_code: int, end_code: int) -> None:
    row = ''
    counter = 0
    
    for char in range(start_code,end_code + 1 ):
        row += f'{char:03d} {chr(char)}   '
        counter += 1
        if counter == 5:
            print(row.strip(','))
            row = ''
            counter = 0

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
