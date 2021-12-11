def reset(grid):
    for row in grid:
        for octopus in row:
            # If the octopus flashed during this
            # step, reset it's energy level to 0.
            if octopus[1] == True:
                octopus[0] = 0
            octopus[1] = False  # Reset "has flashed" state.


def increment(grid):
    for row in grid:
        for octopus in row:
            octopus[0] += 1


def increment_neighbors(grid, row, col):
    for r in range(max(0, row - 1), min(9, row + 1) + 1):
        for c in range(max(0, col - 1), min(9, col + 1) + 1):
            neighbor = grid[r][c]
            if neighbor == grid[row][col]:
                continue
            neighbor[0] += 1  # Increment energy level


def run():

    # Parse input
    with open("day11_input.txt") as f:
        grid = []
        for row in f.readlines():
            rrow = []
            for octopus in row.strip():
                rrow.append([int(octopus), False])
            grid.append(rrow)

    # Part 1
    part1 = 0
    part2 = 0
    step = 0
    while True:
        # Increase the energy level of all octopuses by 1
        increment(grid)

        while True:
            # Fetch all octopuses that are ready to flash and
            # that have not already flashed this step.
            octopus_ready_to_flash = [
                (octopus, y, x)
                for y, row in enumerate(grid)
                for x, octopus in enumerate(row)
                if octopus[0] > 9 and octopus[1] == False
            ]

            # If there are no octopuses ready to flash
            # we're done flashing in this step.
            if len(octopus_ready_to_flash) == 0:
                break

            # For every ready-to-flash octopus
            # Perform the in the problem
            # specified algorithm.
            for entry in octopus_ready_to_flash:
                octopus, row, col = entry
                increment_neighbors(grid, row, col)
                octopus[1] = True  # Mark it as flashed

            if step < 100:  # Part 1
                part1 += len(octopus_ready_to_flash)

        # Reset the grid
        reset(grid)

        # Check if all 0s (Part 2)
        sum_energy_levels = sum(o[0] for r in grid for o in r)
        if sum_energy_levels == 0:
            part2 = step + 1
            break

        step += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
