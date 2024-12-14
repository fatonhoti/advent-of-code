from PIL import Image
from copy import deepcopy

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
        robots2 = []
        for line in f.readlines():
            p, v = line.strip().split()
            p = list(map(int, p.split("=")[1].split(",")))
            v = list(map(int, v.split("=")[1].split(",")))
            robots.append([p, v])
            robots2.append([p, v])
            tm[p[1]][p[0]] += 1
    

    # part 1
    seconds = 100
    for i in range(len(robots)):
        (px, py), (vx, vy) = robots[i]
        nx = (px + seconds*vx) % W
        ny = (py + seconds*vy) % H
        tm[py][px] -= 1
        tm[ny][nx] += 1
        robots[i][0] = [nx, ny]

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
    for s in range(6350, 6400):
        res = [[0] * W for _ in range(H)]
        for i in range(len(robots2)):
            (px, py), (vx, vy) = robots2[i]
            nx = (px + s*vx) % W
            ny = (py + s*vy) % H
            res[ny][nx] += 1
        create_jpeg_image(res, W, H, f"{s}.jpg")


if __name__ == "__main__":
    run()
