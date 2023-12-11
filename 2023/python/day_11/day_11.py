from collections import defaultdict
from math import comb
import itertools

def d(c1, c2, er, ec):
  y1, x1 = c1
  y2, x2 = c2

  dist_x = abs(x1 - x2)
  dist_y = abs(y1 - y2)

  n_gaps = 0

  rng = range(x1 + 1, x2) if x2 > x1 else range(x2 + 1, x1)
  n_gaps += sum(1 for c in rng if ec[c])

  rng = range(y1 + 1, y2) if y2 > y1 else range(y2 + 1, y1)
  n_gaps += sum(1 for r in rng if er[r])
  
  dist = dist_x + dist_y

  return dist, n_gaps

def run():

  expanded_rows = defaultdict(lambda x:False)
  expanded_cols = defaultdict(lambda x:False)
  grid = []
  galaxies = []
  
  with open("day_11.txt", "r") as f:
    for r, line in enumerate(f.readlines()):
      row = []
      for c, cell in enumerate(line.strip()):
        row.append(cell)
        if cell == "#":
          galaxies.append((r, c))
      grid.append(row)
      # Need to expand vertically?
      expanded_rows[r] = all(x == "." for x in row)

  # Need to expand horizontally?
  rotated_grid = [list(elem) for elem in zip(*grid[::-1])]
  for i, row in enumerate(rotated_grid):
    expanded_cols[i] = all(x == "." for x in row)

  # Part 1 & 2
  s1 = 0
  s2 = 0
  for start, end in itertools.combinations(galaxies, 2):
    original_distance, n_gaps = d(start, end, expanded_rows, expanded_cols)
    s1 += original_distance + n_gaps * (2 - 1)
    s2 += original_distance + n_gaps * (1000000 - 1)
  print(f"Part 1: {s1}")
  print(f"Part 2: {s2}")


if __name__ == "__main__":
    run()
