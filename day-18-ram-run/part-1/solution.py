import sys

sys.setrecursionlimit(100000)

grid = [[10000 for _ in range(71)] for _ in range(71)]
lines = [line for line in sys.stdin]
for line in lines[:1024]:
    x, y = [int(i) for i in line.split(",")]
    grid[y][x] = -1

def visit(x0, y0):
    for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x1 = x0 + dx
        y1 = y0 + dy
        if x1 < 0 or x1 >= 71 or y1 < 0 or y1 >= 71:
            continue

        if grid[y1][x1] == -1:
            continue

        if grid[y0][x0] + 1 >= grid[y1][x1]:
            continue

        grid[y1][x1] = grid[y0][x0] + 1
        visit(x1, y1)

grid[0][0] = 0
visit(0, 0)
print(grid[70][70])

