from collections import defaultdict

def run():
    day_n = __file__.split("\\")[-1][:-3]
    
    max_colors_per_game = dict()
    with open(f"{day_n}.txt", "r") as f:
        for line in f.readlines():
            gid, sets = line.split(":")
            gid = int(gid.split()[1])
            sets = [s.strip() for s in sets.split(";")]
            m = defaultdict(int)
            for s in sets:
                for cube in s.split(", "):
                    amount, color = cube.split()
                    amount = int(amount)
                    m[color] = max(m[color], amount)
            max_colors_per_game[gid] = (m["red"], m["green"], m["blue"])

    s1 = 0
    s2 = 0
    for game_id, (mr, mg, mb) in max_colors_per_game.items():
        if mr <= 12 and mg <= 13 and mb <= 14:
            s1 += game_id
        s2 += mr * mg * mb

    print(f"Part 1: {s1}")
    print(f"Part 2: {s2}")

if __name__ == "__main__":
    run()
