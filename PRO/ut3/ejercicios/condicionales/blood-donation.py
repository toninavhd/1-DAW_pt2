def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    
    if 18 <= age <= 65 and weight > 50 and 50 <= heartbeat <= 110 and platelets >= 150_000:
        suitable_for_donation = True
    else:
        suitable_for_donation = False

    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
