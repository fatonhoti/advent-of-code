from collections import Counter


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        left = []
        right = []
        for line in f.readlines():
            a, b = line.strip().split()
            left.append(int(a))
            right.append(int(b))

    part1 = 0
    part2 = 0
    cnt = Counter(right)
    left.sort()
    right.sort()
    for i in range(len(left)):
        li = left[i]
        part1 += abs(li - right[i])
        part2 += cnt[li] * li

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
