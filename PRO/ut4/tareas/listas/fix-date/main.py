def run(input_date: str, base_year: int) -> str:
    date = input_date.split('/')

    month = int(date[0])
    day = int(date[1])
    year = int(date[2]) + base_year

    formated_date = [f'{day:02d}',f'{month:02d}',f'{year:04d}']
    output_date = '-'.join(formated_date)

    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
