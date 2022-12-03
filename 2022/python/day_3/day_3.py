import string

a1 = {l: v + 1 for v, l in enumerate(string.ascii_lowercase)}
a2 = {l: 26 + v + 1 for v, l in enumerate(string.ascii_uppercase)}
pts = {**a1, **a2}


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        rss = [line.strip() for line in f.readlines()]

    # Part 1
    s = sum(
        pts["".join(set(rs[: len(rs) // 2]).intersection(set(rs[len(rs) // 2 :])))]
        for rs in rss
    )
    print(f"Part 1: {s}")

    # Part 2
    s = sum(
        pts["".join(set(rss[i]).intersection(set(rss[i + 1]).intersection(set(rss[i + 2]))))]
        for i in range(0, len(rss), 3)
    )
    print(f"Part 2: {s}")

    """
    Part 1: 7967
    Part 2: 2716
    """


if __name__ == "__main__":
    run()
