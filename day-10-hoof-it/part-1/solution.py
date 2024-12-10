import sys

topographic_map = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    topographic_map.append([int(i) for i in line.strip()])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def visit(r0, c0, visited):
    visited[r0][c0] = True
    if topographic_map[r0][c0] == 9:
        return 1

    count = 0
    for (dr, dc) in directions:
        r1 = r0 + dr
        c1 = c0 + dc
        if r1 < 0 or r1 >= len(visited) or c1 < 0 or c1 >= len(visited[r1]):
            continue

        if visited[r1][c1]:
            continue

        if topographic_map[r1][c1] != topographic_map[r0][c0] + 1:
            continue

        count += visit(r1, c1, visited)

    return count

total = 0
for i in range(len(topographic_map)):
    for j in range(len(topographic_map[i])):
        if topographic_map[i][j] != 0:
            continue

        visited = [[False for _ in row] for row in topographic_map]
        total += visit(i, j, visited)

print(total)

