import sys

lines = [line.strip() for line in sys.stdin if len(line.strip()) != 0]
towels = sorted([towel.strip() for towel in lines[0].split(", ")], key=len)

ways = {"": 1} 
atomic_towels = []

def possible(desired):
    if desired in ways:
        return True

    for towel in atomic_towels:
        if desired.startswith(towel) and possible(desired[len(towel):]):
            return True

    return False

for towel in towels:
    if possible(towel):
        continue

    ways[towel] = 1
    atomic_towels.append(towel)

def assemble(desired):
    if desired in ways:
        return ways[desired]

    total = 0
    for towel in towels:
        if len(towel) > len(desired):
           break 

        if desired.startswith(towel):
            total += assemble(desired[len(towel):])

    ways[desired] = total
    return total

total = 0
for desired in lines[1:]:
    total += assemble(desired)

print(total)

