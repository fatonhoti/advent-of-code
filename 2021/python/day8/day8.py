def part1(input):
    pass


def part2(input):
    pass


def determine(signal_patterns):

    signal_mapping = dict()

    """
    Solved using a solution I am dissatisfied with.
    A more elegant solution will be constructed and posted.
    """

    return signal_mapping


def decode(digit_patterns, signal_mapping):
    pass


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
