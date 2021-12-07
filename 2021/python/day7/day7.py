from scipy.optimize import minimize


def fuel_cost_part1(x, crabs):
    return sum(abs(x - crab) for crab in crabs)


def fuel_cost_part_2(x, el):
    return (abs(x - el) * 0.5 * (1 + abs(x - el))).sum()


def run():

    """
    Todays problem is a function minimization problem.
    Given all the crabs positions, we need to find an aligned position 'x' such that

        for part 1 : f(x) = sum from i=0 to i=N of (|crab_i - x|) is as small as possible, N = # of crabs
        The fuel cost in part 1 for each crab is just the difference |crab_i - x|, the sum of those differences is the total fuel cost. We want to minimize it.

        for part 2 : f(x) = sum from i=0 to i=N of (|crab_i - x| * 0.5 * (1 + |crab_i - x|))  is as small as possible. , N = # of crabs
        The fuel cost in part 2 for each crab is just an arithmetic sum, the sum of those sums is the total fuel cost. We want to minimize it.
    """

    # Parse input
    with open("day7_input.txt") as f:
        crabs = [int(n) for n in f.readline().split(",")]

    # Part 1
    aligned_position = round(minimize(fuel_cost_part1, 1, crabs)["x"][0])
    part1 = fuel_cost_part1(aligned_position, crabs)
    print(f"Part 1: {part1}")

    # Part 2
    aligned_position = round(minimize(fuel_cost_part_2, 2, crabs)["x"][0])
    part2 = sum(
        abs(aligned_position - crab) * 0.5 * (1 + abs(aligned_position - crab))
        for crab in crabs
    )
    print(f"Part 1: {part2}")


if __name__ == "__main__":
    run()
