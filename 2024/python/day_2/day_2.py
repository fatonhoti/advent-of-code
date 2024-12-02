def is_report_safe(report):
    is_increasing = report == sorted(report)
    is_decreasing = report == sorted(report, reverse=True)
    valid_diffs = True
    for i in range(len(report) - 1):
        this = report[i]
        next = report[i + 1]
        diff = abs(this - next)
        if diff < 1 or diff > 3:
            valid_diffs = False
            break

    return (is_decreasing or is_increasing) and valid_diffs


def try_fix_report(report):
    for i in range(0, len(report) - 1):
        this = report[i]
        next = report[i + 1]
        diff = abs(this - next)

        # potential problems
        is_invalid_diff = (
            diff < 1 or diff > 3
        )  # difference between the current level and the next is not in [1, 3]
        is_invalid_increasing = (
            next <= this
        )  # next element is smaller, supposed to be bigger
        is_invalid_decreasing = (
            next >= this
        )  # next element is bigger, supposed to be smaller

        # found a problem? remove it and see if the result is safe
        if is_invalid_diff or is_invalid_increasing or is_invalid_decreasing:
            this_removed = report[:i] + report[i + 1:]
            next_removed = report[: i + 1] + report[i + 2:]
            if is_report_safe(this_removed) or is_report_safe(next_removed):
                return True


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        reports = []
        for level in f.readlines():
            reports.append(list(map(int, level.split())))

    part1 = 0
    part2 = 0
    for report in reports:
        if not is_report_safe(report):
            if try_fix_report(report):
                part2 += 1
        else:
            part1 += 1
            part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
