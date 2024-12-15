import sys

grid = []
for i, line in enumerate(sys.stdin):
    if line.startswith("#"):
        grid.append([j for j in line.strip()])
        if "@" in line:
            (r0, c0) = (i, line.index("@"))

    else:
        for direction in line.strip():
            dr = 0
            dc = 0

            if direction == "^":
                dr = -1
            elif direction == "v":
                dr = 1
            elif direction == "<":
                dc = -1
            elif direction == ">":
                dc = 1

            r1 = r0
            c1 = c0
            visited = []
            while grid[r1][c1] != "#":
                if grid[r1][c1] == ".":
                    for j, value in enumerate(visited):
                        grid[r0 + dr * (j + 1)][c0 + dc * (j + 1)] = value
                    grid[r0][c0] = "."

                    r0 += dr
                    c0 += dc
                    break

                visited.append(grid[r1][c1])
                r1 += dr
                c1 += dc

total = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "O":
            total += i * 100 + j

print(total)

