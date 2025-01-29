def run(input_path: str, output_path: str) -> None:

    with open(input_path) as input_file:    
        with open(output_path, 'w') as output_file:
            for line in input_file:
                striped_line = line.lstrip()
                num_hastags = (len(line) - len(striped_line))
                hastags = '#' * num_hastags
                output_file.write(f'{hastags} {striped_line}\n')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
