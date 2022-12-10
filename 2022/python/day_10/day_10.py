def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        instructions = []
        for line in f.readlines():
            ws = line.strip().split(" ")
            if ws[0] == "noop":
                instructions.append((ws[0], 0))
            else:
                instructions.append((ws[0], int(ws[1])))

    # Part 1 & 2
    def draw(crt, sprite, cycle, row):
        crt[cycle] = "#" if (row * 40 + sprite[0]) <= cycle <= (row * 40 + sprite[1]) else "."
    increment_row = lambda cycle : 1 if cycle % 40 == 0 else 0
    add = lambda x, c: c * x if c % 40 == 20 else 0
    cycle = 0
    x = 1
    s = 0
    crt = [*("0"*40)*6]
    sprite = (0, 2)
    row = 0
    for ins, v in instructions:
        for cyc in range(1, 3):
            draw(crt, sprite, cycle, row)
            cycle += 1
            row += increment_row(cycle)
            s += add(x, cycle)
            if ins == "noop":
                break
            if cyc == 2:
                x += v
                sprite = (x - 1, x + 1)
    
    # Answers
    print(f"Part 1: {s}")
    print("Part 2:", end="")
    for i in range(40 * 6):
        if i % 40 == 0:
            print()
        print(crt[i], end="")

    """
    Part 1: 13760
    Part 2:
    ###..####.#..#.####..##..###..####.####.
    #..#.#....#.#.....#.#..#.#..#.#....#....
    #..#.###..##.....#..#....#..#.###..###..
    ###..#....#.#...#...#....###..#....#....
    #.#..#....#.#..#....#..#.#....#....#....
    #..#.#....#..#.####..##..#....####.#....
    RFKZCPEF
    """


if __name__ == "__main__":
    run()
