def temp_factory(schema: str):
    return schema 

def run(schema: str, temp: float) -> float|None:
    if schema == 'c2f':
        return temp * 1.8 + 32
    elif schema == 'f2c':
        return (temp - 32) / 1.8
    elif schema != 'c2f' or schema != 'f2c':
        return None
    
    ftemp = temp_factory(schema)
    return ftemp(temp)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
