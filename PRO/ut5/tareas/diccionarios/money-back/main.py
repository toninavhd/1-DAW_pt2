def run(to_give_back: float, available_currencies: list) -> dict | None:
    money_back = {}
    available_currencies.sort(reverse=True)

    for currency in available_currencies:
        count = to_give_back // currency
        if count > 0:
            money_back[currency] = int(count)
            to_give_back -= currency * count
            
    if to_give_back > 0:
        money_back = None
        
    return money_back


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
