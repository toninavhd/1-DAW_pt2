def run(hours: int, minutes: int, seconds: int) -> float:
    hours_to_milliseconds = hours * 3600000 
    minutes_to_milliseconds = minutes * 60000
    seconds_to_milliseconds = seconds * 1000
    time_since_midnight = hours_to_milliseconds + minutes_to_milliseconds + seconds_to_milliseconds

    return time_since_midnight


if __name__ == '__main__':
    run(0, 1, 1)