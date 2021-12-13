def fold_y(grid, level):
    folded_grid = grid
    # Loop over the rows after the fold-level
    for i in range(level + 1, len(grid)):
        row = grid[i]
        for col, cell in enumerate(row):
            if cell is not None:
                # Flip the cell to the other side of the fold
                folded_grid[level - (i - level)][col] = "#"

    # Cut off the lower half of the grid
    return [folded_grid[i] for i in range(level)]


def fold_x(grid, level):
    folded_grid = grid
    for r, row in enumerate(grid):
        # Loop over the rows after the fold-level
        for col in range(level + 1, len(grid[0])):
            cell = row[col]
            if cell is not None:
                # Flip the cell to the other side of the fold
                folded_grid[r][level - (col - level)] = "#"

    # Cut off the right side of the grid
    return [row[:level] for row in folded_grid]


def fold_grid(grid, folds):
    folded_grid = grid
    for direction, level in folds:
        if direction == "y":
            folded_grid = fold_y(folded_grid, level)
        else:
            folded_grid = fold_x(folded_grid, level)
    return folded_grid


def run():

    # Parse input
    with open("day13_input.txt") as f:
        points = []
        folds = []
        for line in f.readlines():
            if line[0] == "f":
                direction, level = line.strip().split("=")
                folds.append((direction[-1], int(level)))
            else:
                x, y = line.strip().split(",")
                points.append((int(x), int(y)))

        # Build an emptyg grid
        cols = max(x for x, _ in points) + 1
        rows = max(y for _, y in points) + 1
        grid = [[None for _ in range(cols)] for _ in range(rows)]

        # Populate the grid
        for col, row in points:
            grid[row][col] = "#"

    final_grid = fold_grid(grid, folds)

    # Part 1
    part1 = sum(
        1 for row in fold_grid(grid, [folds[0]]) for cell in row if cell is not None
    )
    print(f"Part 1: {part1}")

    # Part 2
    print("Part 2:")
    print("-" * 78)
    for r in final_grid:
        for p in r:
            if p is not None:
                print(p, end=" ")
            else:
                print(" ", end=" ")
        print()
    print("-" * 78)


if __name__ == "__main__":
    run()
