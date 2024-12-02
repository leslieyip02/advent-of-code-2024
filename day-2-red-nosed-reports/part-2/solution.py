import sys

safe = 0

def is_safe(levels):
    increasing = levels[1] > levels[0]
    for i in range(1, len(levels)):
        if increasing:
            diff = levels[i] - levels[i - 1]
            if diff < 1 or diff > 3:
                return False

        else:
            diff = levels[i - 1] - levels[i]
            if diff < 1 or diff > 3:
                return False

    return True

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    levels = [int(i) for i in line.split(" ")]
    if len(levels) == 1:
        safe += 1
        continue

    for i in range(len(levels)):
        sublist = levels[:i] + levels[i + 1:]
        if is_safe(sublist):
            safe += 1
            break

print(safe)

