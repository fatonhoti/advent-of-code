"""
PLEASE BE AWARE: HORRIBLE CODE!!!!!!!!!!!
MAY CAUSE PERMANENT DAMAGE TO EYES!!!!!!!!!!!
THIS IS YOUR LAST WARNING, GO AWAY FOR YOUR OWN SAKE!!!!!!!!!!!

TODO: Rewrite this abomination.
"""

def seed_to_loc(maps, seed):
    #print(seed, end="  ")
    for map_ in maps:
        # Check if seed falls within any of the ranges
        for src_start, (dst_start, rng) in map_.items():
            if seed in range(src_start, src_start + rng):
                offset = seed - src_start
                seed = dst_start + offset
                break
        #print(seed, end="  ")
    #print()
    return seed

def part2(maps, range_):
    rngs = [[range_, False]]
    for map_ in maps:
        # For each interval in this map
        # figure out what to do with all the available ranges.
        
        # Available range falls outside all intervals? => do nothing
        # -.- fully contained within one interval?     => adjust full range accordingly
        # -.- partly overlaps with one ore more intervals? => split into smaller intervals and
        # add to available ranges to carry them to next map.
        
        do_again = True
        while do_again:
            do_again = False
            for i in range(len(rngs)):
                (start, szr), been_checked = rngs[i]
                if been_checked:
                    continue
                endr = start + szr - 1
                # For each interval in this map
                for src, (dst, szi) in map_.items():
                    endi = src + szi - 1
                    # Check if fully containted within this interval
                    if start >= src and endr <= endi:
                        # Adjust full range accordingly
                        offset = dst - src
                        rngs[i][0][0] += offset
                        rngs[i][1] = True
                        break  # Go to next available range
                    
                    # Check if overlaps with this interval
                    ## Left overlap
                    ## adjust left, leave right
                    if (start >= src and start <= endi) and endr > endi:
                        # Adjust left
                        offset = dst - src
                        new_cnt_left = endi - start + 1
                        left_split = [start + offset, new_cnt_left]
                        # Leave right
                        new_cnt_right = endr - (endi + 1) + 1
                        right_split = [endi + 1, new_cnt_right]
                        # Remove olf, and insert both
                        rngs.pop(i)
                        rngs.append([left_split, True])
                        rngs.append([right_split, False])
                        do_again = True
                        break
                    ## Right overlap
                    ## adjust right, leave left
                    if start < src and (src <= endr and endr <= endi):
                        # Leave left
                        new_cnt_left = (src - 1) - start + 1
                        left_split = [start, new_cnt_left]
                        # Adjust right
                        offset = dst - src
                        new_cnt_right = endr - src + 1
                        right_split = [src + offset, new_cnt_right]
                        rngs.pop(i)
                        rngs.append([left_split, False])
                        rngs.append([right_split, True])
                        do_again = True
                        break
                if do_again:
                    break
            #print(map_)
            #print(rngs)
            #print("#" * 20)
        for i in range(len(rngs)):
            rngs[i][1] = False
    # Final ranges are in loc-space, return minimum of starts
    #print(rngs)
    return min([start for (start, _), _ in rngs])
                

def run():
    day_n = __file__.split("\\")[-1][:-3]
    
    with open(f"{day_n}.txt", "r") as f:
    #with open(f"test.txt", "r") as f:
        seeds = [int(n) for n in f.readline().split(": ")[1].split()]
        
        ranges = []
        #seeds_extended = []
        for i in range(0, len(seeds), 2):
            rng = [seeds[i], seeds[i + 1]]
            #seeds_extended += list(range(seeds[i], seeds[i] + seeds[i + 1]))
            ranges.append(rng)
        
        maps = []
        while (line := f.readline()):
            if line == "\n": continue
            m = {}
            while ((mapping := f.readline()) not in {"\n", ""}):
                dst_start, src_start, rng = [int(n) for n in mapping.split()]
                m[src_start] = (dst_start, rng)
            maps.append(m)
        
    # Part 1 (bruteforce)
    min_loc = 1e10
    for seed in seeds:
        mapped = seed_to_loc(maps, seed)
        min_loc = min(min_loc, mapped)
    print(f"Part 1: {min_loc}")  # correct: 173706076
    
    # Part 2 (smarter)
    min_loc = 9999999999999999999999
    for rng in ranges:
        min_loc_for_range = part2(maps, rng)
        min_loc = min(min_loc, min_loc_for_range)
    print(f"Part 2: {min_loc}")  # correct: 11611182
    
if __name__ == "__main__":
    run()
