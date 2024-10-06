def run(nif: str) -> str:
    nif_number = int(nif) % 23
    table_letter = 'TRWAGMYFPDXBNJZSQVHLCKE'    
    wnif = nif + (table_letter[nif_number])
    return wnif


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
