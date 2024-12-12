import sys

grid = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    grid.append(line.strip())

visited = [[False for _ in row] for row in grid]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_within(r, c):
    return not (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]))

def rotate(subgrid):
    return [[subgrid[j][i] for j in range(2, -1, -1)] for i in range(3)]

def is_line(subgrid):
    return not any(subgrid[0]) and all(subgrid[1]) and not any(subgrid[2])

def is_inner(subgrid):
    return not subgrid[0][0] and subgrid[0][1] and subgrid[1][0]

def is_outer(subgrid):
    return not subgrid[0][1] and not subgrid[1][0]

def corners(r0, c0):
    subgrid = [[False for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            r1 = r0 + i - 1
            c1 = c0 + j - 1
            if is_within(r1, c1):
                subgrid[i][j] = grid[r1][c1] == grid[r0][c0]

    adjacents = 0
    for (dr, dc) in directions:
        if subgrid[1 + dr][1 + dc]:
            adjacents += 1

    if adjacents == 0:
        return 4

    # check horizontal line
    if is_line(subgrid) or is_line(rotate(subgrid)):
        return 0

    # check each corner
    # with reference to the top left quadrant,
    #
    # inner corner: 
    # 
    # .X|.
    # XX|.
    # --+-
    # ..|.
    #
    # outer corner:
    # 
    # ..|.
    # .X|X
    # --+-
    # .X|X

    s = 0
    for _ in range(4):
        if is_inner(subgrid) or is_outer(subgrid):
            s += 1
        subgrid = rotate(subgrid)
    return s

def visit(r0, c0):
    visited[r0][c0] = True
    a0 = 1
    s0 = corners(r0, c0)
    for i1, (dr, dc) in enumerate(directions):
        r1 = r0 + dr
        c1 = c0 + dc

        if not is_within(r1, c1) or grid[r1][c1] != grid[r0][c0] or visited[r1][c1]:
            continue

        a1, s1 = visit(r1, c1)
        a0 += a1
        s0 += s1

    return a0, s0

total = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if visited[r][c]:
            continue

        a, s = visit(r, c)
        total += a * s

print(total)

