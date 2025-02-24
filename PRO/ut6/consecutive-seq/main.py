def consecutive_seq(values:list, reps:int):
    rep_counter = 0
    for value in values:
        if value == value[0]:
            rep_counter += 1
            if reps in rep_counter:
                return value



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(consecutive_seq)
