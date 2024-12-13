import sys

def process_coordinates(line):
    return [int(i[2:]) for i in line.split(": ")[1].split(", ")]

def process_machine(current):
    x1, y1 = process_coordinates(current[0])
    x2, y2 = process_coordinates(current[1])
    x3, y3 = process_coordinates(current[2])

    dp = [[None for _ in range(100)] for _ in range(100)]
    dp[0][0] = (0, 0)
    best = 1001
    for i in range(100):
        if i != 0:
            dp[i][0] = (
                dp[i - 1][0][0] + x1,
                dp[i - 1][0][1] + y1
            )
        if dp[i][0] == (x3, y3):
            best = min(i * 3, best)
        if dp[i][0] >= (x3, y3):
            break

        for j in range(1, 100):
            dp[i][j] = (
                dp[i][j - 1][0] + x2,
                dp[i][j - 1][1] + y2,
            )
            if dp[i][j] == (x3, y3):
                best = min(i * 3 + j, best)
            if dp[i][j] > (x3, y3):
                break

    return 0 if best == 1001 else best

total = 0
current = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        total += process_machine(current)
        current = []

    else:
        current.append(line.strip())

print(total)

