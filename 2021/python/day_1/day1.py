def run():
    with open("day1_input.txt") as f:
        input = list(map(int, f.read().split("\n")))

    # Part 1
    ctr = 0
    pre = input[0]
    for el in input[1:]:
        if el > pre:
            ctr += 1
        pre = el
    print(f"Part 1: {ctr}")

    # Part 2
    pre = sum(input[0:3])
    ctr = 0
    lo = 1
    hi = 4
    while hi < len(input) + 1:
        next = sum(input[lo:hi])
        if next > pre:
            ctr += 1
        pre = next
        lo += 1
        hi += 1
    print(f"Part 2: {ctr}")


if __name__ == "__main__":
    run()
