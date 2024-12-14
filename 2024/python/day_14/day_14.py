from PIL import Image

USE_REAL_INPUT = True

def create_jpeg_image(data, width, height, filename):
    img = Image.new('L', (width, height), color=255)
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            if data[y][x] == 0:
                pixels[x, y] = 0
            else:
                pixels[x, y] = 255

    img.save(filename, format='JPEG')


def run():
    day_n = __file__.split("\\")[-1][:-3]
    file = f"{day_n}.txt" if USE_REAL_INPUT else f"test.txt"
    with open(file, "r") as f:
        H = 103
        W = 101
        tm = [[0] * W for _ in range(H)]

        robots = []
        for line in f.readlines():
            p, v = line.strip().split()
            p = list(map(int, p.split("=")[1].split(",")))
            v = list(map(int, v.split("=")[1].split(",")))
            robots.append([p, v])
            tm[p[1]][p[0]] += 1
    

    # part 1
    seconds = 100
    for i in range(len(robots)):
        (px, py), (vx, vy) = robots[i]
        nx = (px + seconds*vx) % W
        ny = (py + seconds*vy) % H
        tm[py][px] -= 1
        tm[ny][nx] += 1

    tl = 0
    for r in range((H - 1) // 2):
        for c in range((W - 1) // 2):
            tl += tm[r][c]
    
    tr = 0
    for r in range((H - 1) // 2):
        for c in range((W - 1) // 2 + 1, W):
            tr += tm[r][c]
    
    br = 0
    for r in range((H - 1) // 2 + 1, H):
        for c in range((W - 1) // 2 + 1, W):
            br += tm[r][c]
    
    bl = 0
    for r in range((H - 1) // 2 + 1, H):
        for c in range((W - 1) // 2):
            bl += tm[r][c]

    part1 = tl * tr * br * bl
    print(f"Part 1: {part1}")

    # part 2
    for s in range(0, 10000):
        # generate the final tilemap
        res = [[0] * W for _ in range(H)]
        for i in range(len(robots)):
            (px, py), (vx, vy) = robots[i]
            nx = (px + s*vx) % W
            ny = (py + s*vy) % H
            res[ny][nx] += 1
        
        # perform a convolution, goal is to find a kernel_size x kernel_size region of robots
        kernel_size = 5
        for r in range(H - kernel_size + 1):
            min_r, max_r = r, r + kernel_size
            for c in range(W - kernel_size + 1):
                min_c, max_c = c, c + kernel_size

                # check if whole region is filled with robots                
                ok = True
                for rr in range(min_r, max_r):
                    for cc in range(min_c, max_c):
                        if res[rr][cc] == 0:
                            ok = False
                            break
                    if not ok:
                        break

                if ok:
                    print(f"Part 2: {s}")
                    create_jpeg_image(res, W, H, f"{s}.jpeg")
                    exit(0)


if __name__ == "__main__":
    run()
