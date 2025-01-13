def run(cinfo: str) -> dict:
    cinfo = cinfo.split(';')
    cities = {}
    for element in cinfo:
        info = element.split(':')
        cities[info[0]] = int(info[1])
    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
