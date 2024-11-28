def run(items: list) -> list:
    result = [items[0]]

    for item in items[1:]:
        if item != result[-1]:
            result.append(item)

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
