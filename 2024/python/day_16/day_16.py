import networkx as nx
from copy import deepcopy
from collections import defaultdict
import heapq

USE_REAL_INPUT = True

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

G = []
G2 = nx.DiGraph()
H, W = None, None

sr, sc = None, None
er, ec = None, None


def pgrid():
    print("#" + "#" * W + "#")
    for row in G:
        print("#", end="")
        for cell in row:
            if cell == ".":
                print(" ", end="")
            else:
                print(cell, end="")
        print("#", end="\n")
    print("#" + "#" * W + "#")


def dot(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2


def inside(r, c):
    return 0 <= r < H and 0 <= c < W


def astar(start, goal):

    def reconstruct_path(cameFrom, curr, dir):
        tot_path = [curr]
        while (curr, dir) in cameFrom:
            curr, dir = cameFrom[(curr, dir)]
            tot_path.append(curr)
        return tot_path[::-1]

    def nbs(node):
        r, c = node
        nbs = []
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if inside(nr, nc) and G[nr][nc] == ".":
                nbs.append( ( (nr, nc), (dr, dc) ) )
        return nbs
    
    def chebyshev(p1, p2):
        r1, c1 = p1
        r2, c2 = p2
        return max(abs(r2 - r1), abs(c2 - c1))

    def turning_penalty(d1, d2):
        dot_prod = dot(d1, d2)
        if dot_prod == 0:
            return 1000
        elif dot_prod == -1:
            return 2000
        return 0

    cameFrom = defaultdict(tuple)

    gScore = defaultdict(lambda: float("inf"))
    gScore[(start, (0, 1))] = 0

    fScore = defaultdict(lambda: float("inf"))
    fScore[(start, (0, 1))] = chebyshev(start, goal)

    frontier = []
    heapq.heappush(frontier, (fScore[(start, (0, 1))], start, (0, 1)))

    while len(frontier) > 0:
        _, curr, curr_dir = heapq.heappop(frontier)

        if curr == goal:
            path = reconstruct_path(cameFrom, curr, curr_dir)
            return path

        for (nb, nb_dir) in nbs(curr):
            tentative_gScore = gScore[(curr, curr_dir)] + chebyshev(curr, nb) + turning_penalty(curr_dir, nb_dir)
            if tentative_gScore < gScore[(nb, nb_dir)]:
                cameFrom[(nb, nb_dir)] = (curr, curr_dir)
                gScore[(nb, nb_dir)] = tentative_gScore
                fScore[(nb, nb_dir)] = tentative_gScore + chebyshev(nb, goal)
                if (nb, nb_dir) not in [(n, d) for _, n, d in frontier]:
                    heapq.heappush(frontier, (fScore[(nb, nb_dir)], nb, nb_dir))

    return None


def run():
    global G, H, W, sr, sc, er, ec, dr, dc

    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        for r, row in enumerate(f.readlines()[1:-1]):
            line = []
            for c, cell in enumerate(row.strip()[1:-1]):
                match cell:
                    case "S":
                        sr, sc = r, c
                        line.append(".")
                    case "E":
                        er, ec = r, c
                        line.append(".")
                    case _:
                        line.append(cell)
                if cell != "#":
                    for dir in dirs:
                        G2.add_node(((r, c), dir))
            G.append(line)
        
        H = len(G)
        W = len(G[0])

    path = astar((sr, sc), (er, ec))
    part1 = len(path) - 1

    r, c = sr, sc
    dr, dc = 0, 1
    for rr, cc in path[1:]:
        v1x, v1y = cc - c, rr - r

        v1_dot_v2 = dot((v1y, v1x), (dr, dc))

        if v1_dot_v2 == 0:
            part1 += 1000
        elif v1_dot_v2 == -1:
            part1 += 2000

        r, c = rr, cc
        dr, dc = v1y, v1x
    
    print(f"Part 1: {part1}")

    for (r, c), (dr, dc) in G2.nodes:
        if ((r + dr, c + dc), (dr, dc)) in G2.nodes:
            G2.add_edge(((r, c), (dr, dc)), ((r + dr, c + dc), (dr, dc)), weight=1)
        G2.add_edge(((r, c), (dr, dc)), ((r, c), (dc, dr)), weight=1000)
        G2.add_edge(((r, c), (dr, dc)), ((r, c), (-dc, dr)), weight=1000)
    
    for dr, dc in dirs:
        G2.add_edge(((er, ec), (dr, dc)), "end", weight=0)
    
    paths = nx.all_shortest_paths(G2, ((sr, sc), (0, 1)), "end", weight="weight")
    part2 = len({node for path in paths for node, _ in path[:-1]})
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
