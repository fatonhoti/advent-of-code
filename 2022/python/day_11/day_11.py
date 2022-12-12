from collections import deque

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

    # Part 1 & 2
    LCM = 13 * 2 * 19 * 11 * 7 * 5 * 3 * 17 * 23
    part_1 = False
    for _ in range(20 if part_1 else 10_000):
        for monkey in monkeys:
            while monkey["items"]:
                monkey["inspected"] += 1
                item = monkey["items"].popleft()
                new = monkey["op"](item) 
                new = new // 3 if part_1 else new % LCM
                to = monkey["test"](new)
                monkeys[to]["items"].append(new)
    inspections = sorted([monkey["inspected"] for monkey in monkeys], reverse=True)
    print(f"Part n: {inspections[0] * inspections[1]}")
    """
    Part 1: 151312
    Part 2: 51382025916
    """


if __name__ == "__main__":
    run()
