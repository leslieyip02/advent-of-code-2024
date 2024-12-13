import sys

def process_coordinates(line):
    return [int(i[2:]) for i in line.split(": ")[1].split(", ")]

def process_machine(current):
    x1, y1 = process_coordinates(current[0])
    x2, y2 = process_coordinates(current[1])
    x3, y3 = process_coordinates(current[2])
    x3 += 10000000000000 
    y3 += 10000000000000

    # gaussian elimination
    ratio = y1 / x1
    y4 = y2 - (y1 / x1) * x2
    y5 = y3 - (y1 / x1) * x3

    b = round(y5 / y4)
    a = round((x3 - b * x2) / x1)
    if a * x1 + b * x2 != x3 or a * y1 + b * y2 != y3:
        return 0

    return int(a * 3 + b)

total = 0
current = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        total += process_machine(current)
        current = []

    else:
        current.append(line.strip())

print(total)

