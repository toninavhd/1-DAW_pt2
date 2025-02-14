def order_by_age(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda x: x['age'])

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(order_by_age)
