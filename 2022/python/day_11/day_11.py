from collections import deque
from copy import deepcopy


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        monkeys = []
        for line in f.read().split("\n\n"):
            _, items, op, test, true, false = [l.strip() for l in line.split("\n")]
            expr = "".join(op.split()[-3:])
            divisor = int(test.split()[-1])
            true = int(true.split()[-1])
            false = int(false.split()[-1])
            monkey_info = {
                "inspected": 0,
                "items": deque([int(item.strip(",")) for item in items.split()[2:]]),
                "op": lambda old, expr=expr: eval(expr),
                "test": lambda item, comparison=f"{true} if item % {divisor} == 0 else {false}": eval(comparison),
            }
            monkeys.append(monkey_info)
        monkeys_2 = deepcopy(monkeys)

    # Part 1
    for _ in range(20):
        for monkey in monkeys:
            while monkey["items"]:
                monkey["inspected"] += 1
                item = monkey["items"].popleft()
                new = monkey["op"](item) // 3
                to = monkey["test"](new)
                monkeys[to]["items"].append(new)
    inspections = sorted([monkey["inspected"] for monkey in monkeys], reverse=True)
    print(f"Part 1: {inspections[0] * inspections[1]}")

    # Part 2
    LCM = 13 * 2 * 19 * 11 * 7 * 5 * 3 * 17 * 23
    for _ in range(10000):
        for monkey in monkeys_2:
            while monkey["items"]:
                monkey["inspected"] += 1
                item = monkey["items"].popleft()
                new = monkey["op"](item) % LCM
                to = monkey["test"](new)
                monkeys_2[to]["items"].append(new)
    inspections = sorted([monkey["inspected"] for monkey in monkeys_2], reverse=True)
    print(f"Part 2: {inspections[0] * inspections[1]}")

    """
    Part 1: 151312
    Part 2: 51382025916
    """


if __name__ == "__main__":
    run()
