import sys

lines = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    lines.append(line.strip())

def print_picture(elapsed):
    grid = [["." for _ in range(101)] for _ in range(103)]
    for line in lines:
        p = [int(i) for i in line.split(" ")[0][2:].split(",")]
        v = [int(i) for i in line.split(" ")[1][2:].split(",")]

        x = (p[0] + v[0] * i) % 101
        y = (p[1] + v[1] * i) % 103

        grid[y][x] = "*"

    for row in grid:
        print("".join(row))

divider = "".join("-" for _ in range(101))
for i in range(5001, 7500, 103):
    print(f"{i}:")
    print(divider)
    print_picture(i)
    print(divider)

# 6752

