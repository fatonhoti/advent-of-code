def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        bps = []
        for bp in f.read().split("\n\n"):
            bps.append([int(c) for c in bp.split("\n")])

    # Part 1 & 2
    A = sorted((sum(bp) for bp in bps), reverse=True)
    print(f"Part 1: {A[0]}")
    print(f"Part 2: {sum(A[:3])}")
    """
    Part 1: 68775
    Part 2: 202585
    """


if __name__ == "__main__":
    run()
