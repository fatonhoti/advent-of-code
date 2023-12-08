from math import gcd

def run():
    day_n = __file__.split("\\")[-1][:-3]

    dirs = ""
    map_ = dict()
    with open(f"{day_n}.txt", "r") as f:
        dirs = f.readline().strip()
        f.readline()
        for line in f.readlines():
            start, pair = line.split(" = ")
            l, r = pair.strip().split(", ")
            map_[start] = (l[1:], r[:-1])

    def goto_z(start_pos, match_all_z=False):
        steps_taken = 0
        pos = start_pos
        dir_idx = -1
        while True:
            steps_taken += 1
            dir_idx = (dir_idx + 1) % len(dirs)
            pos = map_[pos][0] if dirs[dir_idx] == "L" else map_[pos][1]
            if (match_all_z and pos == "ZZZ") or (pos[-1] == "Z"):
                return steps_taken

    # Part 1
    s1 = goto_z("AAA", match_all_z=True)
    print(f"Part 1: {s1}")
    
    # Part 2
    steps = []
    start_positions = [p for p in map_.keys() if p[-1] == "A"]
    for pos in start_positions:
        steps_taken = goto_z(pos, match_all_z=False)
        steps.append(steps_taken)
    
    lcm = lambda a, b : abs(a * b) // gcd(a, b)
    lcm_ = steps[0]
    for n in steps[1:]:
        lcm_ = lcm(lcm_, n)
    print(f"Part 2: {lcm_}")


if __name__ == "__main__":
    run()
