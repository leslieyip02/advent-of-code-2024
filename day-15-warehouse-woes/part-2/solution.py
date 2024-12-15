import sys

grid = []
for i, line in enumerate(sys.stdin):
    if line.startswith("#"):
        row = []
        for letter in line.strip():
            if letter == "@":
                row.append("@")
                row.append(".")
            elif letter == "O":
                row.append("[")
                row.append("]")
            else:
                row.append(letter)
                row.append(letter)
        grid.append(row)

        if "@" in line:
            (r0, c0) = (i, line.index("@") * 2)

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

            if dr == 0:
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

                continue

            r1 = r0 + dr
            if grid[r1][c0] == "#":
                continue

            elif grid[r1][c0] == ".":
                grid[r1][c0] = "@"
                grid[r0][c0] = "."
                r0 = r1
                continue

            def check(r, c, dr):
                if grid[r][c] == "#":
                    return False

                elif grid[r][c] == ".":
                    return True

                if not check(r + dr, c, dr):
                    return False

                if grid[r][c] == "[":
                    if not check(r + dr, c + 1, dr):
                        return False

                elif grid[r][c] == "]":
                    if not check(r + dr, c - 1, dr):
                        return False

                return True

            if not check(r1, c0, dr):
                continue

            def push(r, c, dr):
                if grid[r][c] == "[":
                    push(r + dr, c, dr)
                    push(r + dr, c + 1, dr)
                    grid[r + dr][c] = "["
                    grid[r + dr][c + 1] = "]"
                    grid[r][c] = "."
                    grid[r][c + 1] = "."

                elif grid[r][c] == "]":
                    push(r + dr, c, dr)
                    push(r + dr, c - 1, dr)
                    grid[r + dr][c] = "]"
                    grid[r + dr][c - 1] = "["
                    grid[r][c] = "."
                    grid[r][c - 1] = "."

            push(r1, c0, dr)
            grid[r1][c0] = "@"
            grid[r0][c0] = "."
            r0 = r1

total = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "[":
            total += i * 100 + j

print(total)

