from collections import Counter
from functools import cmp_to_key


def run():
    day_n = __file__.split("\\")[-1][:-3]

    hands = []
    hands2 = []
    with open(f"{day_n}.txt", "r") as f:
        for line in f.readlines():
            hand, bid = line.split()
            bid = int(bid)
            hands.append((hand, bid))
            hands2.append((transform_hand(hand), hand, bid))

    card_to_score = {}
    for value, card in enumerate(
        ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1], 2
    ):
        card_to_score[card] = value

    # Part 1
    hands = sorted(
        hands,
        key=cmp_to_key(
            hand_compare_wrapper(card_scores=card_to_score, tie_with_original=False)
        ),
    )
    s1 = sum(i * bid for i, (_, bid) in enumerate(hands[::-1], 1))
    print(f"Part 1: {s1}")

    # Part 2
    card_to_score["J"] = 1
    hands2 = sorted(
        hands2,
        key=cmp_to_key(
            hand_compare_wrapper(card_scores=card_to_score, tie_with_original=True)
        ),
    )
    s2 = sum(i * bid for i, (_, _, bid) in enumerate(hands2[::-1], 1))
    print(f"Part 2: {s2}")


def hand_compare_wrapper(card_scores, tie_with_original):
    def wrapper(h1, h2):
        return hand_compare(h1, h2, card_scores, tie_with_original)

    return wrapper


def hand_to_type(hand):
    vals = sorted(list(dict(Counter(hand)).values()), reverse=True)
    # high card
    if vals == [1, 1, 1, 1, 1]:
        return 1
    # one pair
    if vals == [2, 1, 1, 1]:
        return 2
    # two pair
    if vals == [2, 2, 1]:
        return 3
    # three of a kind
    if vals == [3, 1, 1]:
        return 4
    # full house
    if vals == [3, 2]:
        return 5
    # four of a kind
    if vals == [4, 1]:
        return 6
    # five of a kind
    if vals == [5]:
        return 7


def hand_compare(hh1, hh2, card_scores, tie_with_original):
    h1 = hh1[0]
    h2 = hh2[0]

    t1 = hand_to_type(h1)
    t2 = hand_to_type(h2)

    if t1 > t2:
        return -1
    if t1 < t2:
        return 1

    if tie_with_original:
        # Set hands back to their original
        h1 = hh1[1]
        h2 = hh2[1]

    # Hands are equal, compare card-wise
    for i in range(len(h1)):
        c1 = h1[i]
        c2 = h2[i]
        if c1 == c2:
            continue

        if card_scores[c1] > card_scores[c2]:
            return -1
        else:
            return 1


def transform_hand(hand):
    if "J" not in hand:
        return hand

    freqs = Counter(hand)
    if freqs.pop("J") == 5:
        return "JJJJJ"

    most_frequent_card = {v: k for k, v in freqs.items()}[max(freqs.values())]
    return hand.replace("J", most_frequent_card)


if __name__ == "__main__":
    run()
