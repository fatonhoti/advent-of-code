USE_REAL_INPUT = True

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = []
H = 0
W = 0
seen = set()

def inside(r, c):
    return (0 <= r < H) and (0 <= c < W)

def dfs(sr, sc):
    region = grid[sr][sc]
    
    # used for part 2
    def same(r, c, dr, dc):
        rr = r + dr
        cc = c + dc
        return inside(rr, cc) and grid[rr][cc] == region

    stk = [(sr, sc)]
    area = 0
    perim = 0
    sides = 0
    while stk:
        nr, nc = stk.pop()
        if (nr, nc) in seen:
            continue
        seen.add((nr, nc))
        area += 1
        for i, (dr, dc) in enumerate(dirs):
            nbr = nr + dr
            nbc = nc + dc
            if (not inside(nbr, nbc)) or (grid[nbr][nbc] != region):
                perim += 1
            elif (nbr, nbc) not in seen:
                stk.append((nbr, nbc))
            
            # part 2
            d1r, d1c = dr, dc
            d2r, d2c = dirs[(i + 1) % len(dirs)]
            s1 = same(nr, nc, d1r, d1c)
            s2 = same(nr, nc, d2r, d2c)

            # (convex) or (concave)
            if (not s1 and not s2) or (s1 and s2 and not same(nr, nc, d1r + d2r, d1c + d2c)):
                sides += 1
    
    return area, perim, sides


def run():
    global grid, H, W
    
    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        for r, row in enumerate(f.readlines()):
            grid.append(row.strip())

    H = len(grid)
    W = len(grid[0])

    part1 = 0
    part2 = 0
    for r in range(H):
        for c in range(W):
            if (r, c) not in seen:
                a, p, s = dfs(r, c)
                part1 += a * p
                part2 += a * s

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
