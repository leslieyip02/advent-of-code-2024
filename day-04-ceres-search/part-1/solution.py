import sys

directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

def search(grid, row, col):
    count = 0
    for direction in directions:
        letters = []
        for k in range(4):
            i = row + direction[0] * k
            j = col + direction[1] * k
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                continue
            letters.append(grid[i][j])

        if "".join(letters) == "XMAS":
            count += 1

    return count

grid = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    grid.append(line)

total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        total += search(grid, row, col)

print(total)

