def run(speed_km_h: float) -> float:   
    speed_cm_s = (speed_km_h * 1000 * 100) // 3600

    return speed_cm_s


if __name__ == '__main__':
    run(1.08)