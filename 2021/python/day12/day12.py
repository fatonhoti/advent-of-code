from collections import Counter


def dfs(graph):
    paths = []
    stack = [["start"]]
    visited = set()
    while len(stack) > 0:
        path = stack.pop()

        # Update the visited set to only include relevant nodes
        # from the current path
        visited = set([node for node in visited if node in path])

        # If the path has reached the end, the path is done.
        if path[-1] == "end":
            paths.append(path)
        else:
            if path[-1].islower():
                visited.add(path[-1])
            for edge_to in graph[path[-1]]:
                if edge_to not in visited:
                    stack.append([*path, edge_to])
    return paths


def dfs2(graph):
    paths = []
    stack = [["start"]]
    visited = set()
    while len(stack) > 0:
        path = stack.pop()

        # Update the visited set to only include relevant nodes
        # from the current path
        visited = set(
            node for node in visited if node in path and path.count(node) == 2
        )

        # A path can only have one "start" and one "end" node.
        if path.count("start") > 1 or path.count("end") > 1:
            continue

        # If we've traversed more than one small cave twice, it's an illegal path
        if (
            len([cnt for k, cnt in Counter(path).items() if k.islower() and cnt == 2])
            > 1
        ):
            continue

        # If the path has reached the end, the path is done.
        if path[-1] == "end":
            paths.append(path)

        else:
            # We only add small caves that we've traversed twice
            # to the "don't traverse again for this path" set.
            if path[-1].islower() and path.count(path[-1]) == 2:
                visited.add(path[-1])
            for edge_to in graph[path[-1]]:
                # Only allowed to traverse a single small cave max twice.
                if edge_to.islower() and edge_to in visited:
                    continue
                else:
                    stack.append([*path, edge_to])
    return paths


def run():

    # Parse input
    with open("day12_input.txt") as f:
        edges = [n.strip().split("-") for n in f.readlines()]
        graph = {}
        for node_from, node_to in edges:
            if node_from not in graph:
                graph[node_from] = []
            graph[node_from].append(node_to)
            if node_to not in graph:
                graph[node_to] = []
            graph[node_to].append(node_from)

    # Part 1
    paths = dfs(graph)
    print(f"Part 1: {len(paths)}")

    # Part 2
    import time

    start_time = time.time()
    paths = dfs2(graph)
    print(f"Part 2: {len(paths)}")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    run()
