def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        crates = [[] for _ in range(9)]
        for i in range(8):
            line = f.readline().strip()
            for j, c in enumerate(line):
                if c != '.':
                    crates[j] += c
        for i in range(len(crates)):
            crates[i] = crates[i][::-1]
    
        moves = [line.strip() for line in f.readlines()]

    for move in moves:
        _,cr,_,fr,_,to = [int(k) if k.isnumeric() else k for k in move.split()]
        if False:
            # Part 1
            for _ in range(cr):
                crates[to - 1] += crates[fr - 1].pop()
        else:
            # Part 2
            crates[to - 1] += crates[fr - 1][-cr:]
            del crates[fr - 1][-cr:]
    
    for crate in crates:
        print(crate[-1], end="")
    
    """
    Part 1: WHTLRMZRC
    Part 2: GMPMLWNMG
    """


if __name__ == "__main__":
    run()
