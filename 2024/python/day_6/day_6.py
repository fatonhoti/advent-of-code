def simulate_part1(px, py, dx, dy, grid):
    N = len(grid)
    M = len(grid[0])

    seen = set()
    seen.add(py * M + px)

    i = 0
    while True:
        if i > (4 * N * M):
            # loop!
            return 0
        i += 1

        nx = px + dx
        ny = py + dy
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            break
        elif grid[ny][nx] == "#":
            # 90 deg clockwise turn given that +y is downwards => (x, y) => (y, -x)
            dx, dy = -dy, dx
        else:
            px = nx
            py = ny
            seen.add(py * M + px)

    return len(seen), seen


def simulate_part2(px, py, dx, dy, grid, seen):
    M = len(grid[0])
    part2 = 0
    for idx in seen:
        x = idx % M
        y = idx // M
        grid[y][x] = "#"
        if simulate_part1(px, py, dx, dy, grid) == 0:
            part2 += 1
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

    px = py = None
    dx, dy = (0, -1)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in {"<", "^", ">", "v"}:
                px, py = x, y

                part1, seen = simulate_part1(px, py, dx, dy, grid)
                print(f"Part 1: {part1}")

                part2 = simulate_part2(px, py, dx, dy, grid, seen)
                print(f"Part 2: {part2}")

                exit(0)


if __name__ == "__main__":
    run()
