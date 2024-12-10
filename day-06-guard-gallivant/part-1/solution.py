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

visited = [[0 for _ in row] for row in grid]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def trace(row, col, direction_index):
    mask = 1 << direction_index
    if visited[row][col] & mask != 0:
        return
    visited[row][col] |= mask

    new_row = row + directions[direction_index][0]
    new_col = col + directions[direction_index][1]

    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[new_row]):
        return

    elif grid[new_row][new_col] == "#":
        trace(row, col, (direction_index + 1) % 4)

    else:
        trace(new_row, new_col, direction_index)

trace(start_row, start_col, 0)
print(sum([sum([1 for cell in row if cell != 0]) for row in visited]))

