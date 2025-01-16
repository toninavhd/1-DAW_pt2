def run(imoves: str) -> dict:
    inventory = {}
    imoves = imoves.split(',')
    
    for move in imoves:
        merch = move[0]
        amount = int(move[1:])
        if merch in inventory:
            inventory[merch] += amount
        else:
            inventory[merch] = amount
        

    return inventory


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
