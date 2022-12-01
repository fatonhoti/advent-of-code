from operator import mul
from functools import reduce


def get_neighbors(heightmap, row, col):
    # Get neighbors
    neighbors = []

    # Top neighbor
    if row - 1 >= 0:
        neighbors.append((heightmap[row - 1][col], row - 1, col))

    # Bottom neighbor
    if row + 1 < len(heightmap):
        neighbors.append((heightmap[row + 1][col], row + 1, col))

    # Left neighbor
    if col - 1 >= 0:
        neighbors.append((heightmap[row][col - 1], row, col - 1))

    # Right neighbor
    if col + 1 < len(heightmap[0]):
        neighbors.append((heightmap[row][col + 1], row, col + 1))

    return neighbors


def low_point(h, heightmap, row, col):
    neighbors = get_neighbors(heightmap, row, col)
    for neighbor in neighbors:
        if int(h) >= int(neighbor[0]):
            # We can't be standing on a low-point
            # if we have a neighbor with lower height.
            return 0

    return 1 + int(h)


def get_all_low_points(heightmap):
    low_points = []
    for row, heights in enumerate(heightmap):
        for col, height in enumerate(heights):
            if height == "9":
                continue
            if low_point(height, heightmap, row, col) > 0:
                low_points.append((height, row, col))
    return low_points


def run():

    # Parse input
    with open("day9_input.txt") as f:
        heightmap = [line.strip() for line in f.readlines()]

    low_points = get_all_low_points(heightmap)

    # Part 1
    sum_risk_levels = sum(int(h) + 1 for h, _, _ in low_points)
    print(f"Part 1: {sum_risk_levels}")

    # Part 2
    basin_sums = {lp: 0 for lp in low_points}
    for row, heights in enumerate(heightmap):
        for col, height in enumerate(heights):
            if height == "9":
                continue
            r = row
            c = col
            while True:  # Walk down to closest low_point
                next = min(get_neighbors(heightmap, r, c))
                if next in basin_sums.keys():
                    basin_sums[next] += 1
                    break
                r = next[1]
                c = next[2]
    part2 = reduce(mul, sorted((v for v in basin_sums.values()), reverse=True)[:3], 1)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
