def run(stock: dict, merch: str, amount: int) -> bool:
    available = False

    if merch in stock and stock[merch] >= amount:
        available = True

    return available


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
