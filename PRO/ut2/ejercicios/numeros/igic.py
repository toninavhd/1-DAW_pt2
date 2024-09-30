def run(price_with_igic: float, igic: float) -> float:
    
    clean_price = price_with_igic /  ((igic / 100) + 1)

    return round(clean_price, 2)


if __name__ == '__main__':
    run(120, 7)