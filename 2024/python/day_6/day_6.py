def oob(x, y, nRows, nCols):
    return y < 0 or y >= nRows or x < 0 or x >= nCols


def simulate_part1(px, py, dx, dy, grid, max_iterations=None):
    N = len(grid)
    M = len(grid[0])
    seen = set()
    seen.add((px, py))

    i = 0
    while True:
        nx = px + dx
        ny = py + dy

        if max_iterations and i >= max_iterations:
            return None

        if oob(nx, ny, N, M):
            break
        elif grid[ny][nx] == "#":
            # 90 deg clockwise turn given that +y is downwards => (x, y) => (y, -x)
            t = dy
            dy = dx
            dx = -t
        else:
            px = nx
            py = ny
            seen.add((px, py))

        i += 1

    return len(seen)


def simulate_part2(px, py, dx, dy, grid):
    N = len(grid)
    M = len(grid[0])

    orgx, orgy = px, py
    orgdx, orgdy = dx, dy

    part2 = 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] == ".":
                # set blocker on this cell
                grid[y][x] = "#"

                # returns None if loop identified
                if simulate_part1(orgx, orgy, orgdx, orgdy, grid, max_iterations=N * M) == None:
                    part2 += 1

                # reset cell
                grid[y][x] = "."

    return part2


def run():
    USE_REAL_INPUT = True

    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        grid = []
        for row in f.readlines():
            grid.append(list(row.strip()))

    # find the guard
    px = py = dx = dy = None
    found = False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (cell := grid[y][x]) in {"<", "^", ">", "v"}:
                px, py = x, y
                dx, dy = {
                    "<": [-1, 0],
                    "^": [0, -1],
                    ">": [1, 0],
                    "v": [0, 1],
                }[cell]
                found = True
                break
        if found:
            break

    part1 = simulate_part1(px, py, dx, dy, grid)
    print(f"Part 1: {part1}")

    part2 = simulate_part2(px, py, dx, dy, grid)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
