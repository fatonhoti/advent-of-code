from collections import Counter
from functools import cmp_to_key

card_to_score = {}
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
for value, card in enumerate(cards[::-1], 2):
    card_to_score[card] = value


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

    # Part 1
    hands = sorted(hands, key=cmp_to_key(hand_compare_wrapper(card_to_score, False)))
    s1 = 0
    for i, (_, bid) in enumerate(hands[::-1], 1):
        s1 += i * bid
    print(f"Part 1: {s1}")

    # Part 2
    card_to_score["J"] = 1
    hands2 = sorted(hands2, key=cmp_to_key(hand_compare_wrapper(card_to_score, True)))
    s2 = 0
    for i, (_, _, bid) in enumerate(hands2[::-1], 1):
        s2 += i * bid
    print(f"Part 2: {s2}")


def hand_compare_wrapper(card_scores, tie_with_original):
    def wrapper(h1, h2):
        return hand_compare(h1, h2, card_scores, tie_with_original)

    return wrapper


def hand_to_type(hand):
    cnt = dict(Counter(hand))
    vals = sorted(list(cnt.values()), reverse=True)

    # high card
    if len(cnt) == len(hand):
        return 1

    # one pair
    if vals[0] == 2 and vals[1] == 1 and vals[2] == 1 and vals[-1] == 1:
        return 2

    # two pair
    if vals[0] == 2 and vals[1] == 2 and vals[-1] == 1:
        return 3

    # three of a kind
    if vals[0] == 3 and vals[1] == 1 and vals[-1] == 1:
        return 4

    # full house
    if vals[0] == 3 and vals[1] == 2:
        return 5

    # four of a kind
    if vals[0] == 4 and vals[-1] == 1:
        return 6

    # five of a kind
    if len(cnt) == 1:
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

    def get_best_hand(original_hand, cards, current_best, current_hand):
        if not original_hand:
            if len(current_best) == 0:
                current_best.append(current_hand)
            else:
                current_best[0] = (
                    current_hand
                    if hand_compare(
                        [current_hand], [current_best[0]], card_to_score, False
                    )
                    == -1
                    else current_best[0]
                )
            return

        card = original_hand[0]
        rest_hand = original_hand[1:]
        if card == "J":
            # The card is a joker, create new hands
            # where each new hand replaces current "J" with other card
            for card in cards[card]:
                get_best_hand(rest_hand, cards, current_best, current_hand + card)
        else:
            # The card was not a joker, add back the original card to the hand
            # and on to the next
            get_best_hand(rest_hand, cards, current_best, current_hand + card)

    best_reworked_hand = []
    get_best_hand(
        hand,
        {"J": ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]},
        best_reworked_hand,
        "",
    )
    return best_reworked_hand[0]


if __name__ == "__main__":
    run()
