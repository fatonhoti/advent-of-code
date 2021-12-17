from math import sqrt, ceil


def simulate_probe(init_dx, init_dy, x_range, y_range):
    probe = {"x": 0, "y": 0, "dx": init_dx, "dy": init_dy, "max_y": 0}
    while True:
        # Update the position of the probe
        probe["x"] += probe["dx"]
        probe["y"] += probe["dy"]
        if probe["y"] > probe["max_y"]:
            probe["max_y"] = probe["y"]

        # Check if the probe is in the target area
        if probe["x"] in x_range and probe["y"] in y_range:
            return True, probe["max_y"]

        # Check if overshot in x- or y direction
        if probe["x"] > x_range[-1] or y_range[0] < 0 and probe["y"] < y_range[0]:
            break

        # Update dx
        if probe["dx"] > 0:
            probe["dx"] -= 1

        if probe["dx"] < 0:
            probe["dx"] += 1

        # Update dy
        probe["dy"] -= 1

    return False, None


def run():

    # Parse input
    with open("day17_input.txt") as f:
        line = f.readline().strip().split(": ")[1].split(", ")

        x_min_max = tuple(map(int, line[0][2:].split("..")))
        x_range = tuple(x for x in range(x_min_max[0], x_min_max[1] + 1))

        y_min_max = tuple(map(int, line[1][2:].split("..")))
        y_range = tuple(y for y in range(y_min_max[0], y_min_max[1] + 1))

    # The minimum dx can be to even end up in the range.
    min_dx = ceil(sqrt(2 * x_min_max[0] + (1 / 4)) - (1 / 2))

    heights = []
    for dy in range(y_range[0], 1000):
        for dx in range(min_dx, x_range[-1] + dy - y_range[0] + 1):
            velocity_good, max_y = simulate_probe(dx, dy, x_range, y_range)
            if velocity_good:
                heights.append(max_y)

    # Part 2
    part1 = max(heights)
    print(f"Part 1: {part1}")

    # Part 1
    part2 = len(heights)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
