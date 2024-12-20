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

dfs_from_end = [[-1 if i == "#" else int(1e18) for i in row] for row in grid]
dfs_from_end[re][ce] = 0
flood(re, ce, dfs_from_end)

total = 0
for r0 in range(1, len(grid) - 1):
    for c0 in range(1, len(grid[r0]) - 1):
        if grid[r0][c0] == "#":
            continue

        for dr in range(-20, 21):
            for dc in range(-20, 21):
                dt = abs(dr) + abs(dc)
                if dt > 20:
                    continue

                r1 = r0 + dr 
                c1 = c0 + dc
                if r1 < 1 or r1 >= len(grid) - 1 or c1 < 1 or c1 >= len(grid[r1]) - 1:
                    continue

                if grid[r1][c1] == "#":
                    continue

                saved = base - (times[r0][c0] + dt + dfs_from_end[r1][c1])
                if saved >= 100:
                    total += 1

print(total)

