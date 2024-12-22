import sys

def mix(x, y):
    return x ^ y;

def prune(x):
    return x % 16777216

def evolve(x):
    x = mix(x, x * 64)
    x = prune(x)

    x = mix(x, x // 32)
    x = prune(x)

    x = mix(x, x * 2048)
    x = prune(x)

    return x

total = 0
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    x = int(line)
    for _ in range(2000):
        x = evolve(x)
    total += x

print(total)

