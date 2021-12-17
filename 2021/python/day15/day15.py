from collections import defaultdict
import heapq as heap


def extract_path(parentsMap, graph):
    last = list(graph.keys())[-1]
    cost = int(last[0])
    while True:
        last = parentsMap[last]
        if last == list(graph.keys())[0]:
            break
        cost += int(last[0])
    return cost


def get_neighbors(risk_levels, row, col):
    # Get neighbors
    neighbors = []

    # Top neighbor
    if row - 1 >= 0:
        neighbors.append((risk_levels[row - 1][col], row - 1, col))

    # Bottom neighbor
    if row + 1 < len(risk_levels):
        neighbors.append((risk_levels[row + 1][col], row + 1, col))

    # Left neighbor
    if col - 1 >= 0:
        neighbors.append((risk_levels[row][col - 1], row, col - 1))

    # Right neighbor
    if col + 1 < len(risk_levels[0]):
        neighbors.append((risk_levels[row][col + 1], row, col + 1))

    return neighbors


def dijkstra(graph):

    keys = list(graph.keys())

    source_vertex = keys[0]
    target_vertex = keys[-1]

    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float("inf"))
    nodeCosts[source_vertex] = 0
    heap.heappush(pq, (0, source_vertex))

    while pq:
        _, node = heap.heappop(pq)
        visited.add(node)

        if node == target_vertex:
            break

        for neighbor in graph[node]:
            if neighbor in visited:
                continue

            newCost = nodeCosts[node] + int(neighbor[0])
            if nodeCosts[neighbor] > newCost:
                parentsMap[neighbor] = node
                nodeCosts[neighbor] = newCost
                heap.heappush(pq, (newCost, neighbor))

    return parentsMap, nodeCosts


def new_row(old, i):
    row = ""
    for c in old:
        if int(c) + i > 9:
            row += "1"
        else:
            row += str(int(c) + i)
    return row


def run():

    # Parse input
    with open("day15_input.txt") as f:
        grid = []
        grid_expanded = []
        for row in f.readlines():
            row = row.strip()
            grid.append(row)
            temp = row

            # Loop only used to later build graph for part 2
            for _ in range(1, 5):
                new = new_row(temp, 1)
                row += new
                temp = new
            grid_expanded.append(row)

        # Loop only used to later build graph for part 2
        temp_grid = grid_expanded.copy()
        for _ in range(1, 5):
            new_grid = []
            for row in temp_grid:
                nr = new_row(row, 1)
                new_grid.append(nr)
            grid_expanded = [*grid_expanded, *new_grid]
            temp_grid = new_grid

        # Construct graph for part 1
        graph1 = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                graph1[(grid[r][c], r, c)] = get_neighbors(grid, r, c)

        # Construct graph for part 2
        graph2 = {}
        for r in range(len(grid_expanded)):
            for c in range(len(grid_expanded[0])):
                graph2[(grid_expanded[r][c], r, c)] = get_neighbors(grid_expanded, r, c)

    # Part 1
    parentsMap1, _ = dijkstra(graph1)
    part1 = extract_path(parentsMap1, graph1)
    print(f"Part 1: {part1}")

    # Part 2
    parentsMap2, _ = dijkstra(graph2)
    part2 = extract_path(parentsMap2, graph2)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
