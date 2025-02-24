def consecutive_seq(values:list, reps:int):
    rep_counter = values[0]
    for value in values:
        if value in values[1:]:
            if value == rep_counter[-1]:
                rep_counter.append(value)

        return len(rep_counter)
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(consecutive_seq)
