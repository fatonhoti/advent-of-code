from copy import deepcopy
from collections import deque

USE_REAL_INPUT = True

move_to_vec = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1]
}

grid = []
H = None
W = None


def pgrid():
    print("##" + "#" * W + "##")
    for row in grid:
        print("##", end="")
        for cell in row:
            if cell == ".":
                print(" ", end="")
            else:
                print(cell, end="")
        print("##")
    print("##" + "#" * W + "##")


def inside(r, c):
    return 0 <= r < H and 0 <= c < W


def move(sr, sc, dr, dc):
    global grid

    tr = sr + dr
    tc = sc + dc
    if not inside(tr, tc):
        return False

    me = grid[sr][sc]
    next = grid[tr][tc]
    
    if next == "#":
        return False
    elif me == "O" and next == ".":
        grid[tr][tc] = "O"
        grid[sr][sc] = "."
        return True
    elif me == "@" and next == ".":
        grid[tr][tc] = "@"
        grid[sr][sc] = "."
        return True
    elif next == "O":
        can_move = move(tr, tc, dr, dc)
        if can_move:
            if me == "O":
                grid[tr][tc] = "O"
            elif me == "@":
                grid[tr][tc] = "@"
            grid[sr][sc] = "."
            return True
        return False
    else:
        return False


def move2(sr, sc, dr, dc):
    global grid

    orig = deepcopy(grid)

    nr = sr + dr
    nc = sc + dc

    if not inside(nr, nc):
        return False

    next = grid[nr][nc]
    if next == "#":
        return False
    
    if next == ".":
        grid[nr][nc] = "@"
        grid[sr][sc] = "."
        return True

    doable = set()

    to_move = set()
    to_check = deque()
    if next == "]":
        to_move.add(((nr, nc - 1), (nr, nc)))
        to_check.append(((nr, nc - 1), (nr, nc)))
    else:
        to_move.add(((nr, nc), (nr, nc + 1)))
        to_check.append(((nr, nc), (nr, nc + 1)))

    seen = set()
    while to_check:
        curr = to_check.popleft()
        (lr, lc), (rr, rc) = curr

        if (lr, lc, rr, rc) in seen:
            continue

        seen.add((lr, lc, rr, rc))

        nlr, nlc = lr + dr, lc + dc
        nrr, nrc = rr + dr, rc + dc

        if not inside(nlr, nlc) or not inside(nrr, nrc):
            # We tried to move the box out of bounds, no bueno!
            continue

        if grid[nlr][nlc] == "#" or grid[nrr][nrc] == "#":
            # We tried to move box into a wall, no bueno!
            continue

        if grid[nlr][nlc] == "[":
            # There's a box directly above us.
            to_move.add(((nlr, nlc), (nrr, nrc)))
            to_check.append(((nlr, nlc), (nrr, nrc)))

        elif grid[nlr][nlc] == "]" and grid[nrr][nrc] == ".":
            # There's a box up-left above us
            to_move.add(((nlr, nlc - 1), (nlr, nlc)))
            to_check.append(((nlr, nlc - 1), (nlr, nlc)))

        elif grid[nlr][nlc] == "." and grid[nrr][nrc] == "[":
            # There's a box up-right above us
            to_move.add(((nrr, nrc), (nrr, nrc + 1)))
            to_check.append(((nrr, nrc), (nrr, nrc + 1)))

        elif grid[nlr][nlc] == "]" and grid[nrr][nrc] == "[":
            # There's a box up-left above us AND up-right above us
            to_move.add(((nlr, nlc - 1), (nlr, nlc)))  # left box
            to_check.append(((nlr, nlc - 1), (nlr, nlc)))  # left box

            to_move.add(((nrr, nrc), (nrr, nrc + 1)))  # right box
            to_check.append(((nrr, nrc), (nrr, nrc + 1)))  # right box

        else:
            doable.add(curr)
        
    def move(lr, lc, rr, rc):
        match [dr, dc]:
            case [-1, 0] | [1, 0]:
                grid[lr][lc] = "."
                grid[rr][rc] = "."
                grid[lr + dr][lc + dc] = "["
                grid[rr + dr][rc + dc] = "]"
            case [0, 1]:
                grid[lr][lc] = "."
                grid[lr + dr][lc + dc] = "["
                grid[rr + dr][rc + dc] = "]"
            case [0, -1]:
                grid[rr][rc] = "."
                grid[lr + dr][lc + dc] = "["
                grid[rr + dr][rc + dc] = "]"
            case _:
                # uh oh...
                exit(271828)

    moved = 0
    for tm in list(to_move)[::-1]:
        (lr, lc), (rr, rc) = tm

        if tm in doable:
            move(lr, lc, rr, rc)
            moved += 1
            continue

        match [dr, dc]:
            case [-1, 0] | [1, 0]:
                if inside(lr + dr, lc + dc) and grid[lr + dr][lc + dc] == "." and inside(rr + dr, rc + dc) and grid[rr + dr][rc + dc] == ".":
                    move(lr, lc, rr, rc)
                    moved += 1
            case [0, 1]:
                if inside(rr + dr, rc + dc) and grid[rr + dr][rc + dc] == ".":
                    move(lr, lc, rr, rc)
                    moved += 1
            case [0, -1]:
                if inside(lr + dr, lc + dc) and grid[lr + dr][lc + dc] == "." :
                    move(lr, lc, rr, rc)
                    moved += 1
            case _:
                # uh oh...
                exit(271828)

    if moved != len(to_move):
        grid = orig
        return False

    grid[nr][nc] = "@"
    grid[sr][sc] = "."

    return True


def run():
    global grid, H, W

    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        g, mvs = f.read().split("\n\n")
        sr, sc = None, None
        for r, line in enumerate(g.split("\n")[1:-1]):
            line = line.strip()[1:-1]
            row = []
            for c, cell in enumerate(line):
                if cell == "@":
                    sr = r
                    sc = 2 * c
                    row.append("@")
                    row.append(".")
                elif cell == "." or cell == "#":
                    row.append(cell)
                    row.append(cell)
                else:
                    row.append("[")
                    row.append("]")
            grid.append(row)

        H = len(grid)
        W = len(grid[0])
        
        moves = "".join(mvs.split("\n"))
    
    """
    # part 1
    for mv in moves:
        dr, dc = move_to_vec[mv]
        if move(sr, sc, dr, dc):
            sr += dr
            sc += dc
    
    part1 = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "O":
                part1 += 100 * (r + 1) + (c + 1)
    print(f"Part 1: {part1}")
    """

    # part 2
    #pgrid()
    for mv in moves:
        #print(f"move = {mv}")
        #print("-----------------------------------------")
        dr, dc = move_to_vec[mv]
        if move2(sr, sc, dr, dc):
            sr += dr
            sc += dc
        #pgrid()
        #input()
    
    pgrid()

    part2 = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            #if r != 1:
            #    continue
            if cell == "[":
                #print("min_r", r + 1, H - r)
                #print("min_c", c + 2, W - c)
                #dist_r = min(r + 1, H - r)
                #dist_c = min(c + 2, W - c + 2)
                part2 += 100 * (r + 1) + c + 2
                #part2 += 100 * (dist_r) + dist_c
                #print("100*min_r + min_c", 100 * (dist_r) + dist_c)
                #print("-")

    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
