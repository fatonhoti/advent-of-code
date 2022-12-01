def calculate(*, segments, do_part_2=False):
    points = {}
    for segment in segments:
        p1 = segment[0]  # (x1, y1)
        p2 = segment[1]  # (x2, y2)
        covered_points = []
        if p1[0] == p2[0]:  # Vertical segment
            if p1[1] > p2[1]:  # y1 > y2?
                p1, p2 = p2, p1
            covered_points = [(p1[0], y) for y in range(p1[1], p2[1] + 1)]
        elif p1[1] == p2[1]:  # Horizontal segment
            if p1[0] > p2[0]:  # x1 > x2?
                p1, p2 = p2, p1
            covered_points = [(x, p1[1]) for x in range(p1[0], p2[0] + 1)]
        elif do_part_2:  # Diagonal segment
            k = 1 if (p2[1] - p1[1]) / (p2[0] - p1[0]) > 0 else -1
            x = p1[0]
            y = p1[1]
            for _ in range(abs(p1[1] - p2[1]) + 1):
                covered_points.append((x, y))
                x += 1
                y += k

        # Update the map of points and intersections
        for point in covered_points:
            if point not in points:
                points[point] = 0
            points[point] = points[point] + 1

    return sum(1 for _ in filter(lambda p: points[p] >= 2, points))


def run():

    # Parse input
    segments: list[list[tuple(int, int)]] = []
    with open("day5_input.txt") as f:
        for line in f.readlines():
            # segment = [(x1, y1), (x2, y2)]
            segments.append(
                sorted(
                    [
                        (int(p.split(",")[0]), int(p.split(",")[1]))
                        for p in line.split()[::2]
                    ]
                )
            )

    # Part 1 and 2
    part1 = calculate(segments=segments, do_part_2=False)
    part2 = calculate(segments=segments, do_part_2=True)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
