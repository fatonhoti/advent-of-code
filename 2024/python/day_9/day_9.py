from collections import deque, defaultdict

USE_REAL_INPUT = True

q = deque()
id_to_sz = defaultdict(int)
id_to_free = defaultdict(int)
id_to_pos = defaultdict(int)
pos_to_id = defaultdict(int)


def p1():
    qq = deque()
    while q:
        id, f, free_space = q.popleft()
        for _ in range(f):
            qq.append(id)
        
        while q and free_space:
            idd, ff, _ = q[-1]

            if ff > free_space:
                for _ in range(free_space):
                    qq.append(idd)
                q[-1][1] = ff - free_space
                break

            for _ in range(ff):
                qq.append(idd)
            q.pop()
            free_space -= ff
    
    part1 = 0
    i = 0
    while qq:
        id = qq.popleft()
        part1 += i * id
        i += 1
    
    return part1


def p2():
    max_id = max(id_to_sz)
    for file_to_be_moved_id in range(max_id, 0, -1):
        sz = id_to_sz[file_to_be_moved_id]

        files_to_the_left = [idd for idd in id_to_pos if id_to_pos[idd] < id_to_pos[file_to_be_moved_id]]
        for left_file_id in sorted(files_to_the_left, key=lambda id: id_to_pos[id]):
            free = id_to_free[left_file_id]
            if free >= sz:
                pos_to_id.pop(id_to_pos[file_to_be_moved_id])

                start_pos = id_to_pos[left_file_id] + id_to_sz[left_file_id]
                id_to_pos[file_to_be_moved_id] = start_pos

                pos_to_id[start_pos] = file_to_be_moved_id

                id_to_free[left_file_id] = 0
                id_to_free[file_to_be_moved_id] = free - sz

                break

    part2 = 0
    for pos, id in pos_to_id.items():
        for p in range(pos, pos + id_to_sz[id]):
            part2 += p * id

    return part2
    

def run():
    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        dm = f.readline().strip()
        dm += "0"  # test input is odd, interpreting last file as having 0 free space after it.

    pos = 0
    for id, i in enumerate(range(0, len(dm), 2)):
        sz = int(dm[i])
        free = int(dm[i + 1])

        q.append([id, sz, free])
        id_to_sz[id] = sz
        id_to_free[id] = free
        id_to_pos[id] = pos
        pos_to_id[pos] = id

        pos += sz + free
    
    part1 = p1()
    print(f"Part 1: {part1}")

    part2 = p2()
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    run()
