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

sequences = {}
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    x = int(line)
    history = []
    added = set()
    for _ in range(2000):
        y = evolve(x)
        history.append(y % 10 - x % 10)

        if len(history) >= 4:
            sequence = tuple(history[-4:])
            if sequence not in added:
                sequences[sequence] = sequences.get(sequence, 0) + y % 10
                added.add(sequence)

        x = y

print(max(sequences.values()))

