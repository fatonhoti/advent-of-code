def part1(input):
    return sum(
        sum(1 for digit in digits.split(" ") if len(digit) in [2, 4, 3, 7])
        for _, digits in input
    )


def part2(input):
    part2 = 0
    for signal_patterns, digit_patterns in input:
        signal_patterns = signal_patterns.split(" ")
        digit_patterns = digit_patterns.split(" ")
        mapping = determine(signal_patterns)
        part2 += decode(digit_patterns, mapping)
    return part2


def determine(signal_patterns):
    """
    A more elegant actually general solution is being worked on.
    This solution though works perfectly fine for the exact given problem.
    The idea is analysing the appropriate set operations to make with pen and
    paper in order to solve for each segment and then just implementing the
    operations in code.
    """

    signal_patterns = sorted(signal_patterns, key=len)
    signal_mapping = dict()

    one = signal_patterns[0]
    seven = signal_patterns[1]
    four = signal_patterns[2]
    len_5s = [p for p in signal_patterns if len(p) == 5]

    # Find pattern for digit 3
    len_3s = [d for d in len_5s if len(set(four) & set(d)) == 3]
    for pattern in len_3s:
        if "".join(set(one).difference(pattern)) == "":
            # We can now identify which one is which!
            three = len_3s.pop(len_3s.index(pattern))
            five = len_3s.pop(0)
            break

    signal_for_seg_1 = "".join(set(seven).difference(one))
    signal_mapping[signal_for_seg_1] = "1"

    signal_for_seg_2 = "".join(set(four).difference(three))
    signal_mapping[signal_for_seg_2] = "2"

    signal_for_seg_3 = "".join(set(one).difference(five))
    signal_mapping[signal_for_seg_3] = "3"

    signal_for_seg_7 = "".join((set(three).difference(four)).difference(seven))
    signal_mapping[signal_for_seg_7] = "7"

    signal_for_seg_4 = "".join(
        c for c in set(four).difference(one) if c not in signal_mapping.keys()
    )
    signal_mapping[signal_for_seg_4] = "4"

    signal_for_seg_6 = "".join(c for c in four if c not in signal_mapping.keys())
    signal_mapping[signal_for_seg_6] = "6"

    signal_for_seg_5 = "".join(c for c in "abcdefg" if c not in signal_mapping.keys())
    signal_mapping[signal_for_seg_5] = "5"

    return signal_mapping


def decode(digit_patterns, signal_mapping):
    # A string like "136" tells you that
    # segments 1, 3 and 6 are active.
    # A map of active segments to the digit they create.
    digits = {
        "123567": "0",
        "36": "1",
        "13457": "2",
        "13467": "3",
        "2346": "4",
        "12467": "5",
        "124567": "6",
        "136": "7",
        "1234567": "8",
        "123467": "9",
    }
    num = "".join(
        digits["".join(sorted(signal_mapping[signal] for signal in pattern))]
        for pattern in digit_patterns
    )
    return int(num)


def run():

    # Parse input
    with open("day8_input.txt") as f:
        input = [line.strip().split(" | ") for line in f.readlines()]

    # Part 1
    print(f"Part 1: {part1(input)}")

    # Part 2
    print(f"Part 2: {part2(input)}")


if __name__ == "__main__":
    run()
