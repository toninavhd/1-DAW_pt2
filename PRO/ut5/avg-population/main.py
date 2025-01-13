def run(pdata: dict) -> dict:
    total_population = sum(pdata.values())
    avg_data = {}

    for city, population in pdata.items():
        avg = (population /  total_population) * 100
        avg_data[city] = round(avg, 3)

    return avg_data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
