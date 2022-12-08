def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        grid = [row.strip() for row in f.readlines()]
        N = len(grid[0])
        M = len(grid)

    # Part 1
    s = 4 * (N - 1)
    scores = []
    for row in range(1, N - 1):
        for col in range(1, M - 1):
            cell = grid[row][col]

            # Part 1
            left = grid[row][:col][::-1]
            right = grid[row][col + 1 :]
            top = [r[col] for r in grid[:row]][::-1]
            bot = [r[col] for r in grid[row + 1 :]]
            visible = lambda li: len([n for n in li if n < cell]) == len(li)
            if visible(left) or visible(right) or visible(top) or visible(bot):
                s += 1

            # Part 2
            ds = [0, 0, 0, 0]
            for i, li in enumerate([left, right, top, bot]):
                for n in li:
                    if n < cell:
                        ds[i] += 1
                    elif n >= cell:
                        ds[i] += 1
                        break
            scores.append(ds[0] * ds[1] * ds[2] * ds[3])

    #####################
    print(f"Part 1: {s}")
    print(f"Part 2: {max(scores)}")
    """
    Part 1: 1785
    Part 2: 345168
    """


if __name__ == "__main__":
    run()
