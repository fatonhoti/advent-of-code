def run():
    with open("day2_input.txt") as f:
        instructions = []
        for line in f.readlines():
            temp = line.strip().split(" ")
            instruction = (temp[0], int(temp[1]))
            instructions.append(instruction)

    # Part 1
    depth = 0
    horizontal = 0
    for instruction, magnitude in instructions:
        if instruction == "forward":
            horizontal += magnitude
        elif instruction == "down":
            depth += magnitude
        else:
            depth -= magnitude
    print(f"Part 1: {depth * horizontal}")
    """ Alternate solution:
    depth_up = sum([magnitude for _, magnitude in filter(lambda ins: ins[0] == 'up', instructions)]) * (-1)
    depth_down = sum([magnitude for _, magnitude in filter(lambda ins: ins[0] == 'down', instructions)])
    horizontal = sum([magnitude for _, magnitude in filter(lambda ins: ins[0] == 'forward', instructions)])
    print(f"Part 1: {(depth_up + depth_down) * horizontal}")
    """

    # Part 2
    depth = 0
    horizontal = 0
    aim = 0
    for instruction, magnitude in instructions:
        if instruction == "forward":
            horizontal += magnitude
            depth += aim * magnitude
        if instruction == "down":
            aim += magnitude
        if instruction == "up":
            aim -= magnitude
    print(f"Part 2: {depth * horizontal}")


if __name__ == "__main__":
    run()
