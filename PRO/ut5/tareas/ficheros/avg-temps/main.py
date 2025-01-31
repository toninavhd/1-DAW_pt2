def run(input_path: str, output_path: str) -> None:
    with open(input_path) as input_file:
        with open(output_path, 'w') as output_file:
            for line in input_file:
                temps = line.strip().split(',')
                temps_int = [int(temp) for temp in temps]
                avg_temp = sum(temps_int) / len(temps_int)
                output_file.write(f'{avg_temp:.2f}\n')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
