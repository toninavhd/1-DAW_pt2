def run(input_path: str, output_path: str) -> None:

    with open(input_path) as input_file:
        for line in input_file:
            temps = line.split(',')
            temps = [int(temp) for temp in temps]
        avg_temp = sum(temps) / 31
        avg_temp = round(avg_temp, 2)
        
    with open(output_path, 'w') as output_file:
        output_file.write(f'{avg_temp}\n')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
