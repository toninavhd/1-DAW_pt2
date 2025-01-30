def run(input_path: str, replacements: str, output_path: str) -> None:
    replacement_dict = {pair[0]: pair[1] for pair in replacements.split('|')}
    
    with open(input_path) as f, open(output_path, 'w') as out:
        for line in f:
            for old_char, new_char in replacement_dict.items():
                line = line.replace(old_char, new_char)
            out.write(line)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
