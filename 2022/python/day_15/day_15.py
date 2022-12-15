def manhattan(a, b):
    ar, ac = a
    br, bc = b
    return abs(br - ar) + abs(bc - ac)


def run():
    day_n = __file__.split("\\")[-1][:-3]
    with open(f"{day_n}.txt", "r") as f:
        data = dict()
        for line in f.read().split("\n"):
            sensor, beacon = line.split(":")
            # Sensor
            sc, sr = sensor.split()[-2:]
            sr = int(sr.split("=")[1])
            sc = int(sc.split("=")[1].strip(","))
            # Beacon
            bc, br = beacon.split()[-2:]
            br = int(br.split("=")[1])
            bc = int(bc.split("=")[1].strip(","))

            data[(sr, sc)] = (br, bc)

    def search(target_row):
        pts = set()
        for sensor, beacon in data.items():
            d_to_own_beacon = manhattan(sensor, beacon)
            d_to_target_row = abs(sensor[0] - target_row)
            if d_to_own_beacon >= d_to_target_row:
                # Find all points on the target row that are exactly 'd' units away from sensor
                i = d_to_own_beacon - d_to_target_row
                if sensor[0] == target_row:
                    r = sensor[0]
                    left_cols = range(sensor[1] - i, sensor[1])
                    right_cols = range(sensor[1] + 1, sensor[1] + i)
                    pts |= set(list(zip([r] * len(left_cols), left_cols)))
                    pts |= set(list(zip([r] * len(right_cols), right_cols)))
                else:
                    r = (
                        sensor[0] + d_to_target_row
                        if sensor[0] < target_row
                        else sensor[0] - d_to_target_row
                    )
                    pt = (r, sensor[1])
                    pts.add(pt)
                    for k in range(1, i + 1):
                        pt_l = (r, sensor[1] - k)
                        pt_r = (r, sensor[1] + k)
                        pts.add(pt_l)
                        pts.add(pt_r)
        return pts

    # Part 1
    pts = search(2_000_000)
    print(f"Part 1: {len(pts) - 1}")

    # Part 2
    for row in range(4_000_000):

        # Find ranges
        nb_list = []
        for sensor, beacon in data.items():
            d_to_b = manhattan(sensor, beacon)
            remaining = d_to_b - abs(sensor[0] - row)
            if remaining >= 0:
                nb_list.append([sensor[1] - remaining, sensor[1] + remaining])

        # Merge ranges
        nb_list.sort(key=lambda r: r[0])  # Sort on left edges
        merged = []
        for i in range(len(nb_list) - 1):
            (l1, r1), (l2, r2) = nb_list[i : i + 2]
            if l1 <= l2 and r1 >= r2:
                nb_list[i + 1] = (l1, r1)
            elif l2 <= r1 <= r2 or l2 == r1 + 1:
                nb_list[i + 1] = [l1, r2]
            else:
                merged.append((l1, r1))
        merged.append(nb_list[-1])

        # Intersection?
        if len(merged) > 1:
            print(f"Part 2: {(merged[0][1] + 1) * 4_000_000 + row}")

    """
    Part 1: 5525990
    Part 2: 11756174628223
    """


if __name__ == "__main__":
    run()
