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

def visit(r0, c0, i0, scores):
    for i1, (dr, dc) in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0))):
        r1 = r0 + dr
        c1 = c0 + dc 
        if grid[r1][c1] == "#":
            continue

        cost = scores[r0][c0] + 1
        if i1 != i0:
            cost += 1000

        if cost < scores[r1][c1]:
            scores[r1][c1] = cost
            visit(r1, c1, i1, scores)

scores = [[int(1e18) for _ in row] for row in grid]
scores[rs][cs] = 0
visit(rs, cs, 0, scores)

def trace(r0, c0, scores, is_path):
    if grid[r0][c0] == "S":
        return True 

    reached = False
    for i, (dr, dc) in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0))):
        r1 = r0 + dr
        c1 = c0 + dc 
        if grid[r1][c1] == "#":
            continue

        j = 1
        while grid[r1][c1] != "#":
            if grid[r1][c1] == "S":
                for k in range(j):
                    is_path[r0 + dr * k][c0 + dc * k] = True
                reached = True
                break

            grid[r1][c1] = "><v^"[i]
            if scores[r1][c1] == scores[r0][c0] - j - 1000:
                if trace(r1, c1, scores, is_path):
                    for k in range(j):
                        is_path[r0 + dr * k][c0 + dc * k] = True
                    reached = True

            r1 += dr
            c1 += dc
            j += 1

    return reached

is_path = [[False for _ in row] for row in grid]
is_path[rs][cs] = is_path[re][ce] = True
trace(re, ce, scores, is_path)
print(sum(sum(1 for i in row if i) for row in is_path))

