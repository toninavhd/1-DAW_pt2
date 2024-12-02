def run(values: list, oper: str) -> bool:
    result = values[0]

    for value in values[1:]:
        if oper == 'and':
            result = result and value
        elif oper == 'or':
            result = result or value
            
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
