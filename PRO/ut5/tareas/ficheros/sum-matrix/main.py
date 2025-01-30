def run(matrix1_path: str, matrix2_path: str, result_path: str) -> None:
    with open(matrix1_path, encoding='utf-8') as matrix1, open(matrix2_path, encoding='utf-8') as matrix2, open(result_path, 'w', encoding='utf-8') as result:
        lines1 = matrix1.readlines()
        lines2 = matrix2.readlines()

        def convert_lines_to_matrix(lines):
            return [[int(num) for num in line.strip().split()] for line in lines]

        matrix1_num = convert_lines_to_matrix(lines1)
        matrix2_num = convert_lines_to_matrix(lines2)

        result_lines = []
        for numbers1, numbers2 in zip(matrix1_num, matrix2_num):
            result_line = ' '.join(str(num1 + num2) for num1, num2 in zip(numbers1, numbers2))
            result_lines.append(result_line)
        
        result.write('\n'.join(result_lines))
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
