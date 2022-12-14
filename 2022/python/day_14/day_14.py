def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        occupied_points = set()
        for line in f.read().split("\n"):
            r = [
                tuple(int(n) for n in pair.split(","))[::-1]
                for pair in line.split(" -> ")
            ]
            for i in range(0, len(r) - 1):
                (ar, ac), (br, bc) = r[i : i + 2]
                if ar == br:  # Horizontal line
                    for j in range(min(ac, bc), max(ac, bc) + 1):
                        occupied_points.add((ar, j))
                elif ac == bc:  # Vertical line
                    for j in range(min(ar, br), max(ar, br) + 1):
                        occupied_points.add((j, ac))

        inlet = (0, 500)  # (row, col)
        highest = max([p[0] for p in list(occupied_points)])

    def simulate(pts):
        i = 0
        while True:
            sr, sc = inlet
            stuck = False
            while sr < highest:
                # Try to move one step down
                if (sr + 1, sc) not in pts:
                    sr += 1
                    continue
                # Try to move down and left
                elif (sr + 1, sc - 1) not in pts:
                    sr += 1
                    sc -= 1
                    continue
                # Try to move down and right
                elif (sr + 1, sc + 1) not in pts:
                    sr += 1
                    sc += 1
                    continue
                else:
                    # Could not move anywhere
                    pts.add((sr, sc))
                    stuck = True
                    break
            if not stuck:
                # sr >= highest => Oh no, fell into the void!
                break
            i += 1
        return i

    def simulate2(pts):
        i = 0
        while True:
            sr, sc = inlet
            while True:
                # Try to move it one step down
                if (sr + 1, sc) not in pts and sr + 1 < highest + 2:
                    sr += 1
                    continue
                # Try to move down and left
                elif (sr + 1, sc - 1) not in pts and sr + 1 < highest + 2:
                    sr += 1
                    sc -= 1
                    continue
                # Try to move down and right
                elif (sr + 1, sc + 1) not in pts and sr + 1 < highest + 2:
                    sr += 1
                    sc += 1
                    continue
                else:
                    # Could not move anywhere
                    pts.add((sr, sc))
                    i += 1
                    break
            if (sr, sc) == inlet:
                return i

    # Part 1
    print(f"Part 1: {simulate(occupied_points.copy())}")

    # Part 2
    print(f"Part 2: {simulate2(occupied_points)}")

    """
    Part 1: 655
    Part 2: 26484
    """


if __name__ == "__main__":
    run()
