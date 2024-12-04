def search(grid, start_position, targets):
    nRows = len(grid)
    nCols = len(grid[0])

    ds = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

    n = 0
    for dr, dc in ds:
        i = 0
        sr, sc = start_position
        while True:
            sr += dr
            sc += dc

            if sr < 0 or sr >= nRows or sc < 0 or sc >= nCols:
                break

            if grid[sr][sc] != targets[i]:
                # this direction doesn't work. abort.
                break

            # we hit target, did we hit end of the line?
            if targets[i] == "S":
                # we found "XMAS"!
                n += 1
                break

            # hit target, but it was not the end of the line...
            # so we keep trucking. E.g. we found "XMA", now looking for "S"
            i += 1

    return n


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        grid = []
        for row in f.readlines():
            grid.append(row.strip())

    def find_all_x(grid, target):
        xs = []
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == target:
                    xs.append((r, c))
        return xs

    # part 1
    part1 = 0
    for sp in find_all_x(grid, "X"):
        part1 += search(grid, sp, ["M", "A", "S"])

    print(f"Part 1: {part1}")

    # part 2
    nRows = len(grid)
    nCols = len(grid[0])
    is_oob = lambda p: p[0] < 0 or p[0] >= nRows or p[1] < 0 or p[1] >= nCols
    cell_at = lambda p: grid[p[0]][p[1]]

    part2 = 0
    for r, c in find_all_x(grid, "A"):
        tl = (r - 1, c - 1)
        tr = (r - 1, c + 1)
        bl = (r + 1, c - 1)
        br = (r + 1, c + 1)
        if is_oob(tl) or is_oob(tr) or is_oob(bl) or is_oob(br):
            continue

        allowed = {"MAS", "SAM"}
        me = grid[r][c]
        diag1 = cell_at(tl) + me + cell_at(br) in allowed
        diag2 = cell_at(tr) + me + cell_at(bl) in allowed
        if diag1 and diag2:
            part2 += 1

    print(f"Part2: {part2}")


if __name__ == "__main__":
    run()
