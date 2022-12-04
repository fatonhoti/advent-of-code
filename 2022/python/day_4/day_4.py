def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        pairs = []
        for line in f.readlines():
            s1, s2 = line.split(",")
            s1 = [int(n) for n in s1.split("-")]
            s2 = [int(n) for n in s2.split("-")]
            pairs.append((s1, s2))

    contains = lambda s1, s2: s1[0] <= s2[0] and s1[1] >= s2[1]

    # Part 1
    s = sum(1 for s1, s2 in pairs if contains(s1, s2) or contains(s2, s1))
    print(f"Part 1: {s}")

    # Part 2
    s = sum(1 for (a, b), (c, d) in pairs if set(range(a, b + 1)) & set(range(c, d + 1)))
    print(f"Part 2: {s}")

    """
    Part 1: 571
    Part 2: 917
    """


if __name__ == "__main__":
    run()
