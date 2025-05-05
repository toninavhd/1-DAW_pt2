def run(rgb_color: str) -> tuple[int, int, int]:
    clear_rgb = rgb_color.strip('()')
    separation = clear_rgb.replace(',', '-', 1)
    div_index = separation.find('-')
    comma_index = separation.find(',')

    red = int(clear_rgb[comma_index:])
    green = int(clear_rgb[comma_index + 1 : div_index])
    blue = int(clear_rgb[: div_index - 1])

    return red, green, blue


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
