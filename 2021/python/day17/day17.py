from math import sqrt, ceil


def launch_probe(init_dx, init_dy, x_range, y_range):
    x = 0
    y = 0
    dx = init_dx
    dy = init_dy
    max_y = 0
    while True:
        # Update probe's position
        x += dx
        y += dy

        # Check if probe overshot
        if y < y_range[0] or x > x_range[-1]:
            break

        # Check if probe in target area
        if x in x_range and y in y_range:
            return True, max_y

        # Update max height reached
        if y > max_y:
            max_y = y

        # Update velocity
        if dx != 0:
            dx -= 1
        dy -= 1

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

    height = 0
    count = 0
    for dy in range(y_range[0], (-1) * y_range[0]):
        for dx in range(min_dx, x_range[-1] + dy - y_range[0] + 1):
            velocity_good, max_y = launch_probe(dx, dy, x_range, y_range)
            if velocity_good:
                count += 1
                if max_y > height:
                    height = max_y

    # Part 1
    part1 = height
    print(f"Part 1: {part1}")

    # Part 2
    part2 = count
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
