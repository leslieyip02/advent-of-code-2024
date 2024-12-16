import sys

sys.setrecursionlimit(10000)

grid = []
for i, line in enumerate(sys.stdin):
    if len(line.strip()) == 0:
        break

    grid.append([i for i in line.strip()])
    if "S" in line:
        rs, cs = i, line.index("S")
    if "E" in line:
        re, ce = i, line.index("E")

def visit(r0, c0, i0, visited):
    for i1, (dr, dc) in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0))):
        r1 = r0 + dr
        c1 = c0 + dc 
        if grid[r1][c1] == "#":
            continue

        cost = visited[r0][c0] + 1
        if i1 != i0:
            cost += 1000

        if cost < visited[r1][c1]:
            visited[r1][c1] = cost
            visit(r1, c1, i1, visited)

visited = [[int(1e18) for _ in row] for row in grid]
visited[rs][cs] = 0
visit(rs, cs, 0, visited)

print(visited[re][ce])

