def run(unsorted_items: dict) -> list[tuple]:
    
    rev_sorted_items = sorted([(v, k) for k, v in unsorted_items.items()])
    sorted_items = [(k, v) for v, k in rev_sorted_items]
    
    return sorted_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
