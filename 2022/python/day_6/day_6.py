def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        stream = f.read()

    # Part 1
    size = 14  # use 4 instead of 14 for part 1
    for i in range(len(stream)):
        if len(set(stream[i:i + size])) == size:
            print(f"Part n: {i + size}")
            break
    """
    Part 1: 1531
    Part 2: 2518
    """

if __name__ == "__main__":
    run()
