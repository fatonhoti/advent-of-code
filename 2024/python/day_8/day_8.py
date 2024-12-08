USE_REAL_INPUT = True

from collections import defaultdict


def find_nodes(a, b, W, H, inf=False):

    def traverse(sx, sy, dx, dy):
        ns = []
        while True:
            sx += dx
            sy += dy
            if not (0 <= sx < W and 0 <= sy < H):
                break
            ns.append((sx, sy))
            if not inf:
                break
        return ns

    x1, y1 = a
    x2, y2 = b

    dx = x2 - x1
    dy = y2 - y1

    nodes = traverse(x1, y1, -dx, -dy) + traverse(x2, y2, dx, dy)
    return nodes


def run():
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
                seen.update(find_nodes(a, b, W, H, inf=False))
                seen2.update(find_nodes(a, b, W, H, inf=True) + [a, b])

    print(f"Part 1: {len(seen)}")
    print(f"Part 2: {len(seen2)}")


if __name__ == "__main__":
    run()
