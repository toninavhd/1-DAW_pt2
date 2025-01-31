def run(input_path: str, replacements: str, output_path: str) -> None:
    replacement_dict = {}
    for word in replacements.split('|'):
        old_char = word[0]
        new_char = word[1]
        replacement_dict[old_char] = new_char
    
    with open(input_path) as f, open(output_path, 'w') as out:
        for line in f:
            for old_char, new_char in replacement_dict.items():
                line = line.replace(old_char, new_char)
            out.write(line)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
