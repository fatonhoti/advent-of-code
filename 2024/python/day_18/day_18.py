from collections import deque

USE_REAL_INPUT = True

day_n = __file__.split("\\")[-1][:-3]
file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
with open(file, "r") as f:
    bytes = []
    for line in f.readlines():
        x, y = map(int, line.strip().split(","))
        bytes.append((y, x))

H = 71
W = 71

G = []
for _ in range(H):
    row = []
    for _ in range(W):
        row.append(".")
    G.append(row)

def bfs(sr, sc, er, ec):
    Q = deque()
    Q.append((sr, sc, 0))
    seen = set()
    seen.add((sr, sc))
    while Q:
        nr, nc, steps_taken = Q.popleft()

        if (nr, nc) == (er, ec):
            return steps_taken

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr, cc = nr + dr, nc + dc
            if (0 <= rr < H and 0 <= cc < W) and ((rr, cc) not in seen) and G[rr][cc] == ".":
                seen.add((rr, cc))
                Q.append((rr, cc, steps_taken + 1))
    
    return -1

########
# part 1
########
for i in range(1024):
    br, bc = bytes[i]
    G[br][bc] = "#"

part1 = bfs(0, 0, H - 1, W - 1)
assert part1 != -1
print(f"Part 1: {part1}")

##########
# part 2 #
##########
part2 = None
for i in range(1024 + 1, len(bytes)):
    br, bc = bytes[i]
    G[br][bc] = "#"

    steps_taken = bfs(0, 0, H - 1, W - 1)
    if steps_taken == -1:
        part2 = (bc, br)
        break

print(f"Part 2: {part2}")