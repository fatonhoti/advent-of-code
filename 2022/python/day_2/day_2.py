def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        rounds = [line.strip().split() for line in f.readlines()]

    points = {"X": 1, "Y": 2, "Z": 3, "WIN": 6, "DRAW": 3}
    win = {"A": "Y", "B": "Z", "C": "X"}
    draw = {"A": "X", "B": "Y", "C": "Z"}
    lose = {"A": "Z", "B": "X", "C": "Y"}

    # Part 1 & 2
    total_score = [0, 0]
    for op, me in rounds:

        # Part 1
        total_score[0] += points[me]
        if draw[op] == me:
            total_score[0] += points["DRAW"]
        elif win[op] == me:
            total_score[0] += points["WIN"]

        # Part 2
        if me == "X":
            total_score[1] += points[lose[op]]
        elif me == "Y":
            total_score[1] += points[draw[op]] + points["DRAW"]
        else:
            total_score[1] += points[win[op]] + points["WIN"]

    print(f"Part 1: {total_score[0]}")
    print(f"Part 2: {total_score[1]}")
    """
    Part 1: 11063
    Part 2: 10349
    """


if __name__ == "__main__":
    run()
