import sys

sys.setrecursionlimit(10000)

grid = []
for i, line in enumerate(sys.stdin):
    if len(line.strip()) == 0:
        break

    if "^" in line:
        start_row = i
        start_col = line.index("^")
        line = line.replace("^", ".")

    grid.append([c for c in line.strip()])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def trace(row, col, direction_index, grid, visited):
    mask = 1 << direction_index
    if visited[row][col] & mask != 0:
        return True
    visited[row][col] |= mask

    new_row = row + directions[direction_index][0]
    new_col = col + directions[direction_index][1]

    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[new_row]):
        return False

    elif grid[new_row][new_col] == "#":
        return trace(row, col, (direction_index + 1) % 4, grid_copy, visited)

    else:
        return trace(new_row, new_col, direction_index, grid_copy, visited)

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i == start_row and j == start_col:
            continue

        if grid[i][j] != ".":
            continue

        grid_copy = [[cell for cell in row] for row in grid]
        grid_copy[i][j] = "#"
        visited = [[0 for _ in row] for row in grid]
        if trace(start_row, start_col, 0, grid_copy, visited):
            total += 1

print(total)

