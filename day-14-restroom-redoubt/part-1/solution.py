import sys

quadrants = [0 for _ in range(4)]

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    p = [int(i) for i in line.split(" ")[0][2:].split(",")]
    v = [int(i) for i in line.split(" ")[1][2:].split(",")]

    x = (p[0] + v[0] * 100) % 101
    y = (p[1] + v[1] * 100) % 103

    if x == 50 or y == 51:
        continue

    x_bit = "0" if x < 50 else "1"
    y_bit = "0" if y < 51 else "1"
    quadrant_index = int(x_bit + y_bit, base=2)
    quadrants[quadrant_index] += 1

factor = 1
for quadrant in quadrants:
    factor *= quadrant

print(factor)

