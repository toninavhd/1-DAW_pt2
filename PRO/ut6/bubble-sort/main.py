def bsort(values:list):
    sorted_list = []
    for value in values:
        if value in values[1:]:
            if value >= sorted_list[-1]:
                sorted_list.append(value)
    return sorted_list


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(bsort)
