def run():
    day_n = __file__.split("\\")[-1][:-3]

    cards = {}
    with open(f"{day_n}.txt", "r") as f:
        for i, line in enumerate([line.strip() for line in f.readlines()]):
            winning, have = line.split(": ")[1].split(" | ")
            winning = {n for n in winning.split()}
            num_matches = sum(1 for n in have.split() if n in winning)
            cards[i + 1] = [num_matches, 1]

    # Part 1
    sum1 = 0
    sum2 = 0
    for card_id, (num_matches, n_copies) in cards.items():
        sum2 += n_copies

        if num_matches == 0:
            continue

        # Part 1
        card_pts = pow(2, max(0, num_matches - 1))
        sum1 += card_pts

        # Part 2
        for i in range(1, num_matches + 1):
            next_card_id = card_id + i
            if next_card_id < len(cards):
                cards[next_card_id][1] += n_copies

    print(f"Part 1: {sum1}")
    print(f"Part 2: {sum2}")


if __name__ == "__main__":
    run()
