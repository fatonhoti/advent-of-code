def is_report_safe(report):
    is_increasing = report == sorted(report)
    is_decreasing = report == sorted(report, reverse=True)
    diffs_ok = True
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            diffs_ok = False
            break

    return (is_decreasing or is_increasing) and diffs_ok


def try_fix_report(report):
    for i in range(0, len(report)):
        this_removed = report[:i] + report[i + 1:]
        if is_report_safe(this_removed):
            return True


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        reports = [list(map(int, level.split())) for level in f.readlines()]

    part1 = 0
    part2 = 0
    for report in reports:
        is_safe = is_report_safe(report)
        if is_safe:
            part1 += 1
        if try_fix_report(report):
            part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
