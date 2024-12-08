from collections import defaultdict


def slope(a, b):
    x1, y1 = a
    x2, y2 = b
    return x2 - x1, y2 - y1


def in_line(a, b):
    x1, y1 = a
    x2, y2 = b
    dx, dy = slope(a, b)
    if x2 > x1:
        while x1 < x2:
            x1 += dx
            y1 += dy
            if x1 == x2 and y1 == y2:
                return True
    elif x1 > x2:
        while x2 < x1:
            x2 -= dx
            y2 -= dy
            if x1 == x2 and y1 == y2:
                return True

    return False


def find_nodes(a, b, W, H, inf=False):


    def traverse(sx, sy, dx, dy):
        in_bounds = lambda c, r: 0 <= c < W and 0 <= r < H
        ns = []
        while True:
            sx += dx
            sy += dy
            if not in_bounds(sx, sy):
                break
            ns.append((sx, sy))
            if not inf:
                break
        return ns

    x1, y1 = a
    x2, y2 = b
    
    dx, dy = slope(a, b)
    nodes = traverse(x2, y2, dx, dy) + traverse(x1, y1, -dx, -dy)
    return nodes


def run():
    USE_REAL_INPUT = True

    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        lines = f.readlines()
        W = len(lines[0].strip())
        H = len(lines)
        freqs = defaultdict(list)
        for r, row in enumerate(lines):
            for c, cell in enumerate(row.strip()):
                if cell != ".":
                    freqs[cell].append((c, r))

    seen = set()
    seen2 = set()
    for _, locs in freqs.items():
        for i in range(len(locs) - 1):
            a = locs[i]
            for j in range(i + 1, len(locs)):
                b = locs[j]
                if in_line(a, b):
                    seen.update(find_nodes(a, b, W, H, inf=False))
                    seen2.update(find_nodes(a, b, W, H, inf=True) + [a, b])

    print(f"Part 1: {len(seen)}")
    print(f"Part 2: {len(seen2)}")


if __name__ == "__main__":
    run()
