from collections import defaultdict

USE_REAL_INPUT = True

day_n = __file__.split("\\")[-1][:-3]
file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
with open(file, "r") as f:
    patterns, designs = f.read().split("\n\n")
    patterns = set([p.strip() for p in patterns.split(",")])
    designs = designs.split("\n")

dp = defaultdict(int)

def dfs(substring):
    if substring in dp:
        return dp[substring]

    if substring == design:
        return 1

    n = 0
    for pattern in patterns:
        res = substring + pattern
        if design.startswith(res):
            if k := dfs(res):
                n += k

    dp[substring] = n
    return dp[substring]

part1 = 0
part2 = 0
for i, design in enumerate(designs):
    if (nof_ways := dfs("")) > 0:
        part1 += 1
        part2 += nof_ways
    dp.clear()


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
