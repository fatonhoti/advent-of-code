def run():
    day_n = __file__.split("\\")[-1][:-3]
    
    with open(f"{day_n}.txt", "r") as f:
        times = [int(n) for n in f.readline().split(":")[1].split()]
        dsts = [int(n) for n in f.readline().split(":")[1].split()]
    
    # Part 1
    a1 = 1
    for T, R in zip(times, dsts):
        ways = 0
        for t in range(0, T + 1):
            if t * (T - t) > R:
                ways += 1
        a1 *= ways
    print(f"Part 1: {a1}")

    # Part 2
    T = int("".join([str(n) for n in times]))
    R = int("".join([str(n) for n in dsts]))
    ways = 0
    for t in range(0, T + 1):
        if t * (T - t) > R:
            ways += 1
    print(f"Part 2: {ways}")

# PS: Nobody has time for quadratic formulas
if __name__ == "__main__":
    run()
