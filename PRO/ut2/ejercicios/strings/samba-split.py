def run(smb_path: str) -> tuple:
    clean_smb_path = smb_path[2:]
    smb_split = clean_smb_path.split('/', 1)

    host = smb_split[0]
    path = '/' + smb_split[1]
    return host, path


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
