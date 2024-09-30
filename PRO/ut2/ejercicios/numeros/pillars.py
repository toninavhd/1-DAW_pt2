def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    cm_gap_pillars = gap_pillars * 100
    inter_distance = (cm_gap_pillars *(num_pillars - 1))  + ( pillar_width * (num_pillars -2))

    return inter_distance


if __name__ == '__main__':
    run(10, 5, 30)