def run(matrix1_path: str, matrix2_path: str, result_path: str) -> None:
    with (
        open(matrix1_path, encoding='utf-8') as matrix1,
        open(matrix2_path, encoding='utf-8') as matrix2,
        open(result_path, 'w', encoding='utf-8') as result,
    ):
        lines1 = matrix1.readlines()
        lines2 = matrix2.readlines()

        matrix1_num = [[int(num) for num in line.strip().split()] for line in lines1]
        matrix2_num = [[int(num) for num in line.strip().split()] for line in lines2]

        for m_values1, m_values2 in zip(matrix1_num, matrix2_num):
            sums = [str(num1 + num2) for num1, num2 in zip(m_values1, m_values2)]
            result.write(' '.join(sums) + '\n')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
