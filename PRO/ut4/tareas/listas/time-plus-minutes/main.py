def run(time: str, offset: int) -> str:
    time = time.split(':')
    h_offset = offset // 60
    min_offset = offset % 60

    hours = h_offset + int(time[0])
    mins = min_offset + int(time[1])

    if mins > 60:
        hours += mins // 60
        mins -= 60
    if hours > 24:
        hours -= 24

    final_time = f'{hours}:{mins}'





    return final_time


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
