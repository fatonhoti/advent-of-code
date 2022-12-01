from collections import defaultdict


def simulate(rules, pair_count, letter_count, days):
    for _ in range(days):
        for pair, count in list(pair_count.items()):
            if count != 0:
                new_character = rules[pair]
                letter_count[new_character] += count
                pair_count[pair] -= count
                pair_count[pair[0] + new_character] += count
                pair_count[new_character + pair[1]] += count
    return max(letter_count.values()) - min(letter_count.values())


def run():

    # Parse input
    with open("day14_input.txt") as f:
        polymer_template = f.readline().strip()
        f.readline()  # Skip the blank line
        rules = dict()
        for rule in f.readlines():
            key, value = rule.strip().split(" -> ")
            rules[key] = value

    letter_count = defaultdict(int)
    pair_count = defaultdict(int)
    for i in range(len(polymer_template) - 1):
        pair_count[polymer_template[i : i + 2]] += 1
        letter_count[polymer_template[i]] += 1
    letter_count[polymer_template[-1]] += 1

    # Part 1
    part1 = simulate(rules, pair_count, letter_count, 10)
    print(f"Part 1: {part1}")

    # Part 2
    part2 = simulate(rules, pair_count, letter_count, 40)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
