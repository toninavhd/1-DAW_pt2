def consecutive_seq(values:list, reps:int):
    if len(values) < reps:
        return None
    if values[:reps] == [values[0]] * reps:
        return values[0]
    
    return consecutive_seq(values[1:], reps)
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(consecutive_seq)
