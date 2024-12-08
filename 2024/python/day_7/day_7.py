from itertools import product


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def conc(a: int, b: int) -> int:
    return int(str(a) + str(b))


def test(y, ns, operators):
    def combs(ns, operators):
        for combination in product(range(len(operators)), repeat=len(ns) - 1):
            yield combination

    for comb in combs(ns, operators):
        res = operators[comb[0]](ns[0], ns[1])
        for i in range(1, len(comb)):
            if res > y:
                break
            res = operators[comb[i]](res, ns[i + 1])

        if res == y:
            return True

    return False


def run():
    USE_REAL_INPUT = True

    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        m = dict()
        for equation in f.readlines():
            test_value, ns = equation.strip().split(":")
            test_value = int(test_value)
            ns = list(map(int, ns.split()))
            m[test_value] = ns

    part1 = 0
    part2 = 0
    for test_value, ns in m.items():
        if test(test_value, ns, [add, mul]):
            part1 += test_value
        if test(test_value, ns, [add, mul, conc]):
            part2 += test_value

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
