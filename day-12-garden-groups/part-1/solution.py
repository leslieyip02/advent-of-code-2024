import sys

grid = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    grid.append(line.strip())

visited = [[False for _ in row] for row in grid]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def visit(r0, c0):
    if visited[r0][c0]:
        return 0, 0

    visited[r0][c0] = True
    a0 = 1
    p0 = 4
    for (dr, dc) in directions:
        r1 = r0 + dr
        c1 = c0 + dc

        if r1 < 0 or r1 >= len(grid) or c1 < 0 or c1 >= len(grid[r1]):
            continue

        if grid[r1][c1] != grid[r0][c0]:
            continue

        a1, p1 = visit(r1, c1)
        a0 += a1
        p0 += p1 - 1

    return a0, p0

total = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if visited[r][c]:
            continue

        a, p = visit(r, c)
        total += a * p

print(total)

