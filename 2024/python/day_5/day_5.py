from collections import defaultdict


def is_report_in_order(m, report):
    N = len(report)
    for i in range(N - 1):
        a = report[i]
        for j in range(i + 1, N):
            b = report[j]
            if b in m and a in m[b]:
                return False

    return True


def fix_report(m, report):
    fixed_report = [report[0]]
    for n in report[1:]:
        inserted = False
        if n in m:
            for i, k in enumerate(fixed_report):
                if k in m[n]:
                    fixed_report = fixed_report[:i] + [n] + fixed_report[i:]
                    inserted = True
                    break

        if not inserted:
            fixed_report.append(n)

    return fixed_report


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        os, rs = f.read().split("\n\n")

        orderings = defaultdict(set)
        for o in os.split("\n"):
            a, b = list(map(int, o.split("|")))
            orderings[a].add(b)

        reports = []
        for r in rs.split("\n"):
            reports.append(list(map(int, r.strip().split(","))))

    part1 = 0
    part2 = 0
    for report in reports:
        ok = is_report_in_order(orderings, report)
        if ok:
            part1 += report[len(report) // 2]
        else:
            fixed_report = fix_report(orderings, report)
            part2 += fixed_report[len(fixed_report) // 2]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
