from collections import defaultdict


def run():
    day_n = __file__.split("\\")[-1][:-3]

    grid = []
    with open(f"{day_n}.txt", "r") as f:
        grid = ["." + line.strip() + "." for line in f.readlines()]

    width = len(grid[0])
    height = len(grid)

    # For part 1
    sum1 = 0

    # For part 2
    gears = defaultdict(list)
    sum2 = 0

    # Solve parts
    row = 0
    col = 0
    while row != height and col != width:
        if not grid[row][col].isdigit():
            row, col = next_entry(row, col, width)
            continue

        # For part 1
        is_adj_to_symbol = False

        # For part 2
        is_adj_to_gear = False
        gear_pos = None

        num = ""
        while grid[row][col].isdigit():
            num += grid[row][col]
            is_adj, pos = is_adjacent_to_symbol(grid, width, height, (row, col))
            if is_adj:
                is_adj_to_symbol = True
                if pos:
                    # Specifically, it is adjacent to a gear.
                    is_adj_to_gear = True
                    gear_pos = pos
                    gears[pos]  # Map gear-pos to numbers: Tuple[int, int] -> List[int]
            row, col = next_entry(row, col, width)
        num = int(num)

        # Part 1
        if is_adj_to_symbol:
            sum1 += num

        # Part 2
        if is_adj_to_gear:
            gears[gear_pos].append(num)
            if len(gears[gear_pos]) == 2:
                n1, n2 = gears[gear_pos]
                sum2 += n1 * n2

    print(f"Part 1: {sum1}")
    print(f"Part 2: {sum2}")


def next_entry(row, col, width):
    old_col = col
    col = (col + 1) % width
    if col < old_col:
        row += 1
    return row, col


def is_adjacent_to_symbol(grid, width, height, pos):
    row, col = pos

    # Calculate bounds
    min_c = max(0, col - 1)
    max_c = min(width - 1, col + 1)
    min_r = max(0, row - 1)
    max_r = min(height - 1, row + 1)

    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            entry = grid[r][c]
            if not entry.isdigit() and entry != ".":
                if entry == "*":
                    # We're especially interested in gears!
                    return True, (r, c)
                return True, None

    return False, None


if __name__ == "__main__":
    run()
