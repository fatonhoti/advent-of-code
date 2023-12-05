def seed_to_loc(maps, seed):
    for map_ in maps:
        for src_start, (dst_start, rng) in map_.items():
            if seed in range(src_start, src_start + rng):
                seed = dst_start + (seed - src_start)
                break # Go to next map
    return seed

def range_to_loc(maps, range_):
    
    # Helpers
    left_end_overlaps = lambda rstart, rend, istart, iend : (istart <= rstart <= iend) and rend > iend
    right_end_overlaps = lambda rstart, rend, istart, iend : rstart < istart and (istart <= rend <= iend)
    
    def evaluate_range(range_, map_):
        rngs = [range_]
        for i in range(len(rngs)):
            range_start, szr = rngs[i]
            range_end = range_start + szr - 1
            for interval_start, (dst, szi) in map_.items():
                interval_end = interval_start + szi - 1
                if range_start >= interval_start and range_end <= interval_end:
                    # Can safely adjust full range
                    offset = dst - interval_start
                    rngs[i][0] += offset
                    break  # Go to next available range

                if left_end_overlaps(range_start, range_end, interval_start, interval_end):
                    offset = dst - interval_start
                    new_sz_left = interval_end - range_start + 1
                    left_split = [range_start + offset, new_sz_left]
                    
                    new_sz_right = range_end - (interval_end + 1) + 1
                    right_split = [interval_end + 1, new_sz_right]
                    
                    rngs.pop(i)
                    rngs.append(left_split)
                    rngs += evaluate_range(right_split, map_)
                    break  # Go to next available range

                if right_end_overlaps(range_start, range_end, interval_start, interval_end):
                    new_sz_left = (interval_start - 1) - range_start + 1
                    left_split = [range_start, new_sz_left]
                    
                    offset = dst - interval_start
                    new_sz_right = range_end - interval_start + 1
                    right_split = [interval_start + offset, new_sz_right]
                    
                    rngs.pop(i)
                    rngs += evaluate_range(left_split, map_)
                    rngs.append(right_split)
                    break  # Go to next available range
        return rngs
        
    rngs = [range_]
    for map_ in maps:
        new_ranges = []
        for i in range(len(rngs)):
            new_ranges += evaluate_range(rngs[i], map_)
        rngs = new_ranges
    return min([s for s, _ in rngs])
                

def run():
    day_n = __file__.split("\\")[-1][:-3]
    
    with open(f"day_5.txt", "r") as f:
        seeds = [int(n) for n in f.readline().split(": ")[1].split()]
        
        ranges = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
        
        maps = []
        while (line := f.readline()):
            if line == "\n": continue
            m = {}
            while ((mapping := f.readline()) not in {"\n", ""}):
                dst_start, src_start, rng = [int(n) for n in mapping.split()]
                m[src_start] = (dst_start, rng)
            maps.append(m)
        
    # Part 1
    min_loc = 9999999999999999999999
    for seed in seeds:
        min_loc = min(min_loc, seed_to_loc(maps, seed))
    print(f"Part 1: {min_loc}")
    
    # Part 2
    min_loc = 9999999999999999999999
    for rng in ranges:
        min_loc = min(min_loc, range_to_loc(maps, rng))
    print(f"Part 2: {min_loc}")

if __name__ == "__main__":
    run()
