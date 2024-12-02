import sys

safe = 0

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    levels = [int(i) for i in line.split(" ")]
    if len(levels) == 1:
        safe += 1
        continue

    increasing = levels[1] > levels[0]
    ok = True
    for i in range(1, len(levels)):
        if increasing:
            diff = levels[i] - levels[i - 1]
            if diff < 1 or diff > 3:
                ok = False
                break

        else:
            diff = levels[i - 1] - levels[i]
            if diff < 1 or diff > 3:
                ok = False
                break

    if ok:
        safe += 1

print(safe)

