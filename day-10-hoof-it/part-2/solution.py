import sys

topographic_map = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    topographic_map.append([int(i) for i in line.strip()])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [[0 for _ in row] for row in topographic_map]

def visit(r0, c0):
    visited[r0][c0] += 1
    if topographic_map[r0][c0] == 9:
        return

    for (dr, dc) in directions:
        r1 = r0 + dr
        c1 = c0 + dc
        if r1 < 0 or r1 >= len(visited) or c1 < 0 or c1 >= len(visited[r1]):
            continue

        if topographic_map[r1][c1] != topographic_map[r0][c0] + 1:
            continue

        visit(r1, c1)

for i in range(len(topographic_map)):
    for j in range(len(topographic_map[i])):
        if topographic_map[i][j] != 0:
            continue

        visit(i, j)

total = 0
for i in range(len(topographic_map)):
    for j in range(len(topographic_map[i])):
        if topographic_map[i][j] != 9:
            continue

        total += visited[i][j]

print(total)

