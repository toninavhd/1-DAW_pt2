def run(arc_A: float) -> float:
    PI = 3.14
    radius =( 4 * arc_A) / (2 * PI)
    area = radius * radius

    return round(area, 10)


if __name__ == '__main__':
    run(1)