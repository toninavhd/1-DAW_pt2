def run(input_path: str, output_path: str) -> None:
    sum_temps = 0

    with open(input_path) as f:
        for line in f:
            temps = line.split(',')
            for temp in temps:
                sum_temps += float(temp)
            avg_temp = sum_temps / 31
            avg_temp = round(avg_temp, 2)

    with open(output_path, 'w') as write_file:
        write_file.write(f'{avg_temp}')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
