from collections import deque

USE_REAL_INPUT = True

grid = []
W = None
H = None


def nbs(r, c):
    # up, right, down, left
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    nbs = []
    for dr, dc in dirs:
        tr = r + dr
        tc = c + dc
        if (0 <= tr < H) and (0 <= tc < W) and (grid[tr][tc] == (grid[r][c] + 1)):
            nbs.append((tr, tc))

    return nbs


def dfs(start):
    n = 0
    seen = set()
    stk = []
    stk.append(start)
    while stk:
        r, c = stk.pop()
        if (r, c) not in seen and grid[r][c] == 9:
            n += 1
            seen.add((r, c))
            continue
        seen.add((r, c))
        for nb in nbs(r, c):
            if nb not in seen:
                stk.append(nb)
    return n


def bfs(start, end):
    seen = set()
    Q = deque()
    Q.append(start)
    n = 0
    while Q:
        r, c = Q.popleft()
        if (r, c) == end:
            n += 1
            seen.add((r, c))
            continue
        seen.add((r, c))
        for nb in nbs(r, c):
            if nb not in seen:
                Q.append(nb)

    return n


def run():
    global W, H

    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        trailheads = []
        trailends = []
        for r, line in enumerate(f.readlines()):
            row = []
            for c, cell in enumerate(line.strip()):
                row.append(int(cell))
                if cell == "0":
                    trailheads.append((r, c))
                elif cell == "9":
                    trailends.append((r, c))
            grid.append(row)

        H = len(grid)
        W = len(grid[0])

    part1 = 0
    for th in trailheads:
        part1 += dfs(th)
    print(f"Part 1: {part1}")

    part2 = 0
    for th in trailheads:
        for te in trailends:
            part2 += bfs(th, te)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
