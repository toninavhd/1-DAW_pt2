def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    age_condition = 18 <= age <= 65
    weight_condition = weight > 50
    heartbeat_condition = heartbeat <= 100
    platelets_condition = platelets > 150_000

    if age_condition and weight_condition and heartbeat_condition and platelets_condition:
        suitable_for_donation = True
    else:
        suitable_for_donation = False

    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
