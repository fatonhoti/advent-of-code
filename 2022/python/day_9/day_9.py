def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        moves = []
        for line in f.readlines():
            a, b = line.strip().split()
            moves.append((a, int(b)))

    dirs = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

    def apply_corrections(links):
        for i in range(len(links) - 1):
            hr, hc = links[i]
            tr, tc = links[i + 1]
            if abs(hc - tc) > 1 or abs(hr - tr) > 1:
                """Horizontal movement (x)"""
                if hc > tc:  # Head moved towards the right
                    tc += 1
                elif hc < tc:  # Head moved towards the left
                    tc -= 1
                """ Vertical movement (y) """
                if hr > tr:  # Head moved downwards
                    tr += 1
                elif hr < tr:  # Head moved upwards
                    tr -= 1
                links[i + 1] = (tr, tc)  # Update the current tail link's position

        # Return the position of the last link as it's the only one of interest
        return links[-1]

    def simulate(body, moves):
        # Head is assumed to be in the front of the list
        visited = set()
        visited.add((0, 0))
        for dir, steps in moves:
            dr, dc = dirs[dir]
            for _ in range(steps):
                body[0] = (body[0][0] + dr, body[0][1] + dc)
                apply_corrections(body)
                visited.add(body[-1])
        return visited

    # Part 1
    p1 = simulate([(0, 0)] * 2, moves)
    p2 = simulate([(0, 0)] * 10, moves)
    print(f"Part 1: {len(p1)}")
    print(f"Part 2: {len(p2)}")
    """
    Part 1: 5883
    Part 2: 2367
    """


if __name__ == "__main__":
    run()
