def run(data: dict, target_value: int) -> list:
    source_keys = []

    for data_key, data_value in data.items():
        if data_value == target_value:
            source_keys.append(data_key)

    source_keys = sorted(source_keys)

    return source_keys


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
