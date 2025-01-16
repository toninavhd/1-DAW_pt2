def run(data: dict, target_keys: tuple) -> dict:
    pdata = {key: data[key] for key in target_keys if key in data} 
    
    return pdata


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
