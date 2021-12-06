from collections import Counter


def simulate(fishes, days):
    for _ in range(days):
        fishes = fishes[1:] + fishes[:1]
        fishes[6] += fishes[-1]
    return sum(fishes)


def run():

    # Parse input
    with open("day6_input.txt") as f:
        initial_state = list(map(int, f.readline().split(",")))

    # Part 1
    fishes = [0] * 9  # fishes[i] gives # of fishes with i days left
    for k, v in dict(Counter(initial_state)).items():
        fishes[k] = v

    fishes_after_80_days = simulate(fishes, days=80)
    print(f"Part 1: {fishes_after_80_days}")

    # Part 2
    fishes_after_256_days = simulate(fishes, days=256)
    print(f"Part 2: {fishes_after_256_days}")


if __name__ == "__main__":
    run()
