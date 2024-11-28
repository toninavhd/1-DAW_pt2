def run(matrix: list) -> int | None:
    
    for row in matrix:
        if len(row) == len(matrix):
            sum_diagonal = 0
            for num in range(len(matrix)):
                sum_diagonal += matrix[num][num]
        else:
            sum_diagonal = None
        

    return sum_diagonal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
