def run():
    def build_tree(fs, directory):
        fs[directory] = []
        while line := f.readline():
            ws = line.split()
            if ws[0] == "cd":
                if ws[1] == "..":
                    return
                d = {ws[1]: []}
                fs[directory].append(d)
                build_tree(d, ws[1])
            elif ws[0] == "dir" or ws[0] == "ls":
                continue
            else:
                fs[directory].append((ws[1], int(ws[0])))  # (filename, size)

    def get_size(dir, dir_sizes):
        size = 0
        for entry in dir:
            if isinstance(entry, dict):
                subdir_size = get_size([*entry.values()][0], dir_sizes)
                size += subdir_size
            else:
                size += entry[1]
        dir_sizes.append(size)
        return size

    def pretty(d, indent=0):
        for key, value in d.items():
            print("\t" * indent + str(key))
            for val in value:
                if isinstance(val, dict):
                    pretty(val, indent + 1)
                else:
                    print("\t" * (indent + 1) + str(val))

    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        tree = {}
        root = "/"
        build_tree(tree, root)
        dir_sizes = []
        tot_size = get_size(tree["/"], dir_sizes)
        space_needed = 30_000_000 - (70_000_000 - tot_size)
        sum_10k = 0
        minimum_dir = 1e9
        for size in dir_sizes:
            sum_10k += size if size <= 100_000 else 0  # Part 1
            if size >= space_needed and size < minimum_dir:  # Part 2
                minimum_dir = size
        print(f"Part 1: {sum_10k}")
        print(f"Part 2: {minimum_dir}")
        """
        Part 1: 1778099
        Part 1: 1623571
        """


if __name__ == "__main__":
    run()
