import re
import sys

mul_pattern = r"mul\(\d+,\d+\)"
num_pattern = r"(\d+),(\d+)"

total = 0

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    for mul in re.findall(mul_pattern, line):
        a, b = [int(i) for i in re.search(num_pattern, mul).group(1, 2)]
        total += a * b

print(total)

