def run():
    day_n = __file__.split("\\")[-1][:-3]
    
    max_colors_per_game = dict()
    with open(f"{day_n}.txt", "r") as f:
        for line in f.readlines():
            gid, sets = line.split(":")
            gid = int(gid.split()[1])
            sets = [s.strip() for s in sets.split(";")]
            max_red = 0
            max_green = 0
            max_blue = 0
            for s in sets:
                for cube in s.split(", "):
                    amount, color = cube.split()
                    amount = int(amount)
                    if color == "red" and amount > max_red:
                        max_red = amount
                    if color == "green" and amount > max_green:
                        max_green = amount
                    if color == "blue" and amount > max_blue:
                        max_blue = amount
            max_colors_per_game[gid] = (max_red, max_green, max_blue)

    # Part 1
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
