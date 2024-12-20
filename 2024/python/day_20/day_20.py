from collections import defaultdict
import heapq

USE_REAL_INPUT = True

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

G = []
H = None
W = None

sr, sc = None, None
er, ec = None, None

day_n = __file__.split("\\")[-1][:-3]
file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
with open(file, "r") as f:
    lines = f.readlines()
    for r, line in enumerate(lines[1:-1]):
        line = line.strip()
        row = []
        for c, cell in enumerate(line[1:-1]):
            if cell == "S":
                sr, sc = r, c
                row.append(".")
            elif cell == "E":
                er, ec = r, c
                row.append(".")
            else:
                row.append(cell)
        G.append(row)

H = len(G)
W = len(G[0])

def inside(r, c):
    return 0 <= r < H and 0 <= c < W

    
def astar(start, goal):

    def nbs(node):
        r, c = node
        nbs = []
        for dr, dc in dirs:
            tr, tc = r + dr, c + dc
            if inside(tr, tc) and G[tr][tc] == ".":
                nbs.append((tr, tc))
        return nbs

    def reconstruct_path(cameFrom, curr):
        tot_path = [curr]
        while curr in cameFrom:
            curr = cameFrom[curr]
            tot_path.append(curr)
        return tot_path[::-1]

    def chebyshev(p1, p2):
        r1, c1 = p1
        r2, c2 = p2
        return max(abs(r2 - r1), abs(c2 - c1))

    cameFrom = defaultdict(tuple)

    gScore = defaultdict(lambda: float("inf"))
    gScore[start] = 0

    fScore = defaultdict(lambda: float("inf"))
    fScore[start] = chebyshev(start, goal)

    frontier = []
    heapq.heappush(frontier, (fScore[start], start))

    while len(frontier) > 0:
        _, curr = heapq.heappop(frontier)

        if curr == goal:
            path = reconstruct_path(cameFrom, curr)
            return path

        for nb in nbs(curr):
            tentative_gScore = gScore[curr] + chebyshev(curr, nb)
            if tentative_gScore < gScore[nb]:
                cameFrom[nb] = curr
                gScore[nb] = tentative_gScore
                fScore[nb] = tentative_gScore + chebyshev(nb, goal)
                if nb not in frontier:
                    heapq.heappush(frontier, (fScore[nb], nb))

    return None


path = astar((sr, sc), (er, ec))
assert path is not None, "No solution... uh oh!"

best_time = len(path) - 1
print(f"Best time = {best_time}")

def get_walls(node, rng):
    r, c = node

    min_r, max_r = max(0, r - rng), min(H - 1, r + rng)
    min_c, max_c = max(0, c - rng), min(W - 1, c + rng)

    nbs = set()
    for rr in range(min_r, max_r + 1):
        for cc in range(min_c, max_c + 1):
            if (rr, cc) == (r, c):
                continue
            ed = abs(rr - r) + abs(cc - c)
            if ed > rng:
                continue
            if inside(rr, cc) and G[rr][cc] == "#":
                nbs.add((rr, cc))

    return nbs

cnt = defaultdict(int)
walls = set()
for r, c in path:
    walls |= get_walls((r, c), 1)

for r, c in walls:
    G[r][c] = "."

    p = astar((sr, sc), (er, ec))
    if (lp := len(p) - 1) < best_time:
        diff = best_time - lp
        cnt[diff] += 1

    G[r][c] = "#"

part1 = 0
for k, v in sorted(cnt.items(), key=lambda k: k[0]):
    #print(f"{v} cheat(s) that saves {k} picoseconds.")
    if k >= 100:
        part1 += v
print(f"Part 1: {part1}")