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

is_valid = lambda r, c: r >= 0 and r < len(antinodes) and c >= 0 and c < len(antinodes[r])

for frequency, locations in antennas.items():
    if len(locations) < 2:
        continue

    for i in range(len(locations)):
        r0, c0 = locations[i]
        antinodes[r0][c0] = True

        for j in range(i + 1, len(locations)):
            r1, c1 = locations[j]

            dr = r1 - r0
            dc = c1 - c0

            r2 = r0 - dr
            c2 = c0 - dc
            while is_valid(r2, c2):
                antinodes[r2][c2] = True
                r2 -= dr
                c2 -= dc

            r3 = r1 + dr
            c3 = c1 + dc
            while is_valid(r3, c3):
                antinodes[r3][c3] = True
                r3 += dr
                c3 += dc

print(sum([row.count(True) for row in antinodes]))

