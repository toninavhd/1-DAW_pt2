def add(values:list)-> int:
    flatten_values = []
    for value in values:
        if isinstance(value,list):
            for value in values:
                flatten_values.append(value)
        if not values:
            return 0

    return add(sum(values))
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(add)
