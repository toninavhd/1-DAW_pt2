def run(farm: list) -> str:
    
    if farm.index("lobo") == len(farm) -1:
            msg = 'No te quiero ver más por aquí, lobo' 
    else:
        reverse_farm = farm[::-1]
        sheep_index = reverse_farm.index("lobo")
        msg = f'Cuidado oveja {sheep_index}, el lobo te va a comer'

    return msg


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
