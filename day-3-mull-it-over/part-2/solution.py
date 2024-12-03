import re
import sys

all_pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
num_pattern = r"(\d+),(\d+)"

enabled = True
total = 0

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    for instruction in re.findall(all_pattern, line):
        mul, do, dont = instruction
        if do:
            enabled = True
        elif dont:
            enabled = False
        else:
            if enabled:
                a, b = [int(i) for i in re.search(num_pattern, mul).group(1, 2)]
                total += a * b

print(total)

