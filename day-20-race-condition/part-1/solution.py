import sys

sys.setrecursionlimit(100000)

grid = []
for i, line in enumerate(sys.stdin):
    if len(line.strip()) == 0:
        break

    grid.append([i for i in line.strip()])
    if "S" in line:
        rs, cs = i, line.index("S")
    if "E" in line:
        re, ce = i, line.index("E")

def flood(r0, c0, times):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        r1 = r0 + dr
        c1 = c0 + dc
        if times[r1][c1] == -1:
            continue

        if times[r0][c0] + 1 < times[r1][c1]:
            times[r1][c1] = times[r0][c0] + 1
            flood(r1, c1, times)

times = [[-1 if i == "#" else int(1e18) for i in row] for row in grid]
times[rs][cs] = 0
flood(rs, cs, times)
base = times[re][ce]

total = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] != "#":
            continue

        times = [[-1 if i == "#" else int(1e18) for i in row] for row in grid]
        times[rs][cs] = 0
        times[i][j] = int(1e18)
        flood(rs, cs, times)
        saved = base - times[re][ce]
        if saved >= 100:
            total += 1

print(total)

