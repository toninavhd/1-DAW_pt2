def run(marks: list) -> tuple:
    avg_marks = sum(marks) / len(marks)

    below_avg = [mark for mark in marks if mark <= avg_marks]
    above_avg = [mark for mark in marks if mark > avg_marks]

    return below_avg, above_avg


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
