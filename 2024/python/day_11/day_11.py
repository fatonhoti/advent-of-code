from collections import defaultdict
from math import log10

USE_REAL_INPUT = True


def split(n, POWERS = [10**i for i in range(10)]):
    digits = int(log10(n)) + 1
    power = POWERS[digits // 2]
    return (n // power, n % power)


def simulate(stones, iters):
    seen = defaultdict(int)
    for stone in stones:
        seen[stone] = 1

    for _ in range(iters):
        t = seen.copy()
        for stone, freq in seen.items():
            if stone == 0:
                t[1] += freq
            elif (int(log10(stone)) + 1) % 2 == 0:
                x1, x2 = split(stone)
                t[x1] += freq
                t[x2] += freq
            else:
                t[stone * 2024] += freq
            t[stone] -= freq
        seen = t

    return sum(seen.values())


def run():
    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        stones = list(map(int, f.readline().strip().split()))

    part1 = simulate(stones, 25)
    print(f"Part 1: {part1}")

    part2 = simulate(stones, 75)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
