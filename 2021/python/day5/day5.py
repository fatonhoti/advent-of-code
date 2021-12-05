def run():
    def is_vertical(line):
        if line[0][0] == line[1][0]:
            return True
        return False

    def is_horizontal(line):
        if line[0][1] == line[1][1]:
            return True
        return False

    def get_covered_points_vertical(start, end):
        covered_points = []
        for y in range(start[1], end[1] + 1):
            point = (start[0], y)
            covered_points.append(point)
        return covered_points

    def get_covered_points_horizontal(start, end):
        covered_points = []
        for x in range(start[0], end[0] + 1):
            point = (x, start[1])
            covered_points.append(point)
        return covered_points

    def get_covered_points_diagonal(start, end):
        covered_points = []
        k = (end[1] - start[1]) / (end[0] - start[0])
        if k < 0:
            # Negative slope
            x = start[0]
            y = start[1]
            for _ in range(start[1] - end[1] + 1):
                point = (x, y)
                covered_points.append(point)
                x += 1
                y -= 1
        else:
            # Positive slope
            x = start[0]
            y = start[1]
            for _ in range(end[1] - start[1] + 1):
                point = (x, y)
                covered_points.append(point)
                x += 1
                y += 1
        return covered_points

    # get_covered_points_diagonal((7, 9), (9, 7))
    # return
    # Parse input
    segments = []
    with open("day5_input.txt") as f:
        # with open("inp.txt") as f:
        for line in f.readlines():
            # print(line.split()[::2])
            segment = [
                (int(p.split(",")[0]), int(p.split(",")[1])) for p in line.split()[::2]
            ]
            segments.append(segment)

    # Part 1
    points = {}
    for segment in segments:
        start = segment[0]
        end = segment[1]
        covered_points = []
        if is_vertical(segment):
            if start[1] < end[1]:  # y1 < y2
                covered_points = get_covered_points_vertical(start, end)
            else:  # y1 > y2
                covered_points = get_covered_points_vertical(end, start)
            for point in covered_points:
                if point not in points:
                    points[point] = 1
                else:
                    points[point] = points[point] + 1
        elif is_horizontal(segment):
            if start[0] < end[0]:  # x1 < x2
                covered_points = get_covered_points_horizontal(start, end)
            else:  # x1 > x2
                covered_points = get_covered_points_horizontal(end, start)
            for point in covered_points:
                if point not in points:
                    points[point] = 1
                else:
                    points[point] = points[point] + 1
        else:
            if start[0] < end[0]:  # x1 < x2
                covered_points = get_covered_points_diagonal(start, end)
            else:  # x1 > x2
                covered_points = get_covered_points_diagonal(end, start)
            for point in covered_points:
                if point not in points:
                    points[point] = 1
                else:
                    points[point] = points[point] + 1
    part1 = 0
    for _, val in points.items():
        if val >= 2:
            part1 += 1
    print(part1)

    # Part 2


if __name__ == "__main__":
    run()
