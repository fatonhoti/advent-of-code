def compare(a, b):

    a = a[::-1]
    b = b[::-1]

    while len(a) > 0 and len(b) > 0:
        left, right = a.pop(), b.pop()
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                continue
            return -1 if left < right else 1
        elif isinstance(left, list) and isinstance(right, int):
            right = [right]
        elif isinstance(left, int) and isinstance(right, list):
            left = [left]
        if res := compare(left, right):
            return res

    if len(a) == 0 and len(b) > 0:
        # Left list ran out of items first, right order!
        return -1

    if len(a) > 0 and len(b) == 0:
        # Right list ran out of items first, incorrect order!
        return 1

    # Could not decide
    return 0


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        packets = []
        for pair in f.read().split("\n\n"):
            packets += [eval(p) for p in pair.split("\n")]

    # Part 1
    s = 0
    pair = 1
    for i in range(0, len(packets) - 2, 2):
        a, b = packets[i : i + 2]
        if compare(a, b) == -1:
            s += pair
        pair += 1
    print(f"Part 1: {s}")

    # Part 2
    from functools import cmp_to_key
    p = sorted(packets + [[[2]]] + [[[6]]], key=cmp_to_key(compare))
    i = p.index([[2]]) + 1
    j = p.index([[6]]) + 1
    print(f"Part 2: {i*j}")

    """
    Part 1: 5003
    Part 2: 20280
    """


if __name__ == "__main__":
    run()
