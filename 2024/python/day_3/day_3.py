import re


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        inp = f.read()

    # matches "mul(x,y)" where x,y are integers with 1-3 digits
    # matches "do()"
    # matches "don't()""
    # returns matches in order left to right
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    instructions = re.findall(pattern, inp)

    part1 = 0
    part2 = 0
    enabled = True
    for instruction in instructions:
        match instruction:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                x, y = instruction.split(",")
                prod = int(x[4:]) * int(y[:-1])
                part1 += prod
                if enabled:
                    part2 += prod

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
