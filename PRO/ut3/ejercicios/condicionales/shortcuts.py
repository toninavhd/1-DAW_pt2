def run(key1: str, key2: str, key3: str) -> str:
    match key1, key2, key3:
        case 'CTRL','ALT','T':
            action = 'Open terminal'
        case 'CTRL','ALT','L':
            action = 'Lock screen'
        case 'CTRL','ALT','D':
            action = 'Show desktop'
        case 'ALT','F2','':
            action = 'Run console'
        case 'CTRL','Q','':
            action = 'Close window'
        case 'CTRL','ALT','DEL' :
            action = 'Log out'
        case _:
            action = 'Undefined'
    return action


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
