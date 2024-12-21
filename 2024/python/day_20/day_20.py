from collections import defaultdict, deque
from copy import deepcopy
import heapq

USE_REAL_INPUT = True

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

G = []
H = None
W = None

start = None
end = None

day_n = __file__.split("\\")[-1][:-3]
file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
with open(file, "r") as f:
    lines = f.readlines()
    for r, line in enumerate(lines[1:-1]):
        line = line.strip()
        row = []
        for c, cell in enumerate(line[1:-1]):
            if cell == "S":
                start = (r, c)
                row.append(".")
            elif cell == "E":
                end =  (r, c)
                row.append(".")
            else:
                row.append(cell)
        G.append(row)

H = len(G)
W = len(G[0])

def inside(r, c):
    return 0 <= r < H and 0 <= c < W

def nbs(node):
    r, c = node
    nbs = []
    for dr, dc in dirs:
        tr, tc = r + dr, c + dc
        if inside(tr, tc) and G[tr][tc] == ".":
            nbs.append((tr, tc))
    return nbs

Q = deque()
Q.append((start, 0, [start]))
seen = set()
seen.add(start)
best_path = None
while Q:
    curr, d, path = Q.popleft()
    if curr == end:
        best_path = path
        break
    for nb in nbs(curr):
        if nb not in seen:
            seen.add(nb)
            Q.append((nb, d + 1, path + [nb]))

best_time = len(best_path) - 1

dist_to_end_from = defaultdict(int)
for d, node in enumerate(best_path):
    dist_to_end_from[node] = best_time - d

def get_shortcuts(node, rng):
    r, c = node

    min_r, max_r = max(0, r - rng), min(H - 1, r + rng)
    min_c, max_c = max(0, c - rng), min(W - 1, c + rng)

    shortcuts = set()
    for rr in range(min_r, max_r + 1):
        for cc in range(min_c, max_c + 1):
            if (rr, cc) == (r, c):
                continue
            ed = abs(rr - r) + abs(cc - c)
            if ed <= rng and inside(rr, cc) and G[rr][cc] == ".":
                shortcuts.add((rr, cc))

    return shortcuts


def go(cheat_time):
    n = 0
    for d_to_curr, (r, c) in enumerate(best_path):
        shortcuts = get_shortcuts((r, c), cheat_time)
        for sr, sc in shortcuts:
            d_to_shortcut = abs(r - sr) + abs(c - sc)
            d_path = d_to_curr + d_to_shortcut + dist_to_end_from[(sr, sc)]
            if d_path <= best_time - 100:
                n += 1
    return n

part1 = go(2)
part2 = go(20)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")