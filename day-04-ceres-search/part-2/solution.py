import sys

grid = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    grid.append(line)

total = 0
for row in range(len(grid) - 2):
    for col in range(len(grid[row]) - 2):
        d1 = "".join(grid[row + i][col + i] for i in range(3))
        d2 = "".join(grid[row + 2 - i][col + i] for i in range(3))
        if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM"):
            total += 1

print(total)

