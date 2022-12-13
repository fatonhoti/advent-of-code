from collections import deque
from string import ascii_lowercase

heights = {c: i for i, c in enumerate(ascii_lowercase)}
heights["S"] = 0
heights["E"] = 25


def neighbours(grid, cell):
    nbs = []
    r, c = cell
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        rt = r + dr[i]
        ct = c + dc[i]
        if (
            ct in range(0, len(grid[0]))
            and rt in range(0, len(grid))
            and heights[grid[rt][ct]] <= heights[grid[r][c]] + 1
        ):
            nbs.append((rt, ct))
    return nbs


def bfs(grid, start, GOAL):
    # Iterative BFS
    Q = deque()
    Q.append((start, []))  # [start] for adding start node too
    visited = set()
    visited.add(start)
    while Q:
        node, path = Q.popleft()
        if (node[0], node[1]) == GOAL:
            return path  # + [node] for adding end node too
        for nb in neighbours(grid, node):
            if nb not in visited:
                visited.add(nb)
                Q.append((nb, path + [nb]))
    # No path to goal found
    return None


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:

        start = None
        end = None
        a_cells = []  # Used in part 2
        grid = []
        for r, row in enumerate(f.read().split("\n")):
            rr = []
            for c, cell in enumerate(row):
                if cell == "S":
                    start = (r, c)
                elif cell == "E":
                    end = (r, c)
                elif cell == "a":
                    a_cells.append((r, c))
                rr.append(cell)
            grid.append(rr)
        
    # Part 1
    path = bfs(grid, start, end)
    print(f"Part 1: {len(path)}")

    # Part 2
    len_paths = []
    for starting_cell in a_cells:
        path = bfs(grid, starting_cell, end)
        if path:
            len_paths.append(len(path))
    print(f"Part 2: {min(len_paths)}")

    """
    Part 1: 408
    Part 2: 399
    """


if __name__ == "__main__":
    run()
    