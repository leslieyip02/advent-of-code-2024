import sys

grid = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    grid.append(line.strip())

antennas = {}
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == '.':
            continue

        antennas[cell] = antennas.get(cell, [])
        antennas[cell].append((i, j))

antinodes = [[False for _ in row] for row in grid]
for frequency, locations in antennas.items():
    if len(locations) < 2:
        continue

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            r0, c0 = locations[i]
            r1, c1 = locations[j]

            dr = r1 - r0
            dc = c1 - c0

            r2 = r0 - dr
            c2 = c0 - dc
            if r2 >= 0 and r2 < len(antinodes) and c2 >= 0 and c2 < len(antinodes[r2]):
                antinodes[r2][c2] = True

            r3 = r1 + dr
            c3 = c1 + dc
            if r3 >= 0 and r3 < len(antinodes) and c3 >= 0 and c3 < len(antinodes[r3]):
                antinodes[r3][c3] = True

print(sum([row.count(True) for row in antinodes]))

