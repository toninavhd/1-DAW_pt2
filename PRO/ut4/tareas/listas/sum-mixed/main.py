def run(items: list) -> int:
    items2int = [int(num) for num in items]

    sum_items = sum(items2int)
    
    return sum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
