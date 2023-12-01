def run():
    day_n = __file__.split("\\")[-1][:-3]

    lines = []
    with open(f"{day_n}.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Part 1
    s1 = 0
    for line in lines:
        first = None
        last = None
        for c in line:
            if c.isdigit():
                last = c
                if first is None:
                    first = c
        s1 += int(first + last)
    print(f"Part 1: {s1}")

    # Part 2
    s2 = 0
    spelled_out = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in lines:
        first = None
        last = None
        for i in range(len(line)):
            one = line[i]
            if one.isdigit():
                last = one
            elif (three := line[i : i + 3]) in spelled_out:
                # one, two, six
                last = spelled_out[three]
            elif (four := line[i : i + 4]) in spelled_out:
                # zero, four, five, nine
                last = spelled_out[four]
            elif (five := line[i : i + 5]) in spelled_out:
                # three, seven, eight
                last = spelled_out[five]
            if first is None:
                first = last
        s2 += int(first + last)
    print(f"Part 2: {s2}")


if __name__ == "__main__":
    run()
