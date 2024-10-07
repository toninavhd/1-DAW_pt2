def run(html: str) -> str:
    hastag_numbers = int(html[2:3])
    clean_html = html[4:-5]
    markdown = (hastag_numbers * '#') + ' ' + clean_html
    return markdown


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
