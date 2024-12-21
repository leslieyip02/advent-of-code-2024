import sys

numeric_positions = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

directional_positions = {
    "^": (0, 1), # ^
    "A": (0, 2), # A
    "<": (1, 0), # <
    "v": (1, 1), # v
    ">": (1, 2), # >
}

def numeric_keypad(target):
    moves = []

    previous = "A"
    for current in target:
        r0, c0 = numeric_positions[previous]
        r1, c1 = numeric_positions[current]

        dr = abs(r1 - r0)
        dc = abs(c1 - c0)

        if r1 < r0:
            if c1 < c0:
                if r0 != 3 or c1 != 0:
                    moves.extend(["<"] * dc)
                moves.extend(["^"] * dr)
                if r0 == 3 and c1 == 0:
                    moves.extend(["<"] * dc)

            else:
                moves.extend(["^"] * dr)
                moves.extend([">"] * dc)

        else:
            if c1 <= c0:
                moves.extend(["<"] * dc)
                moves.extend(["v"] * dr)

            else:
                if r1 != 3 or c0 != 0:
                    moves.extend(["v"] * dr)
                moves.extend([">"] * dc)
                if r1 == 3 and c0 == 0:
                    moves.extend(["v"] * dr)

        moves.append("A")
        previous = current

    return moves

previous = ["A"] * 26
memo = {}

def directional_keypad(current, layer):
    if layer == 0:
        return 1

    initial_previous = previous[layer]
    if (current, layer, initial_previous) in memo:
        total, updates = memo[(current, layer, initial_previous)]
        for i, update in enumerate(updates):
            previous[i] = update
        return total

    total = 0

    r0, c0 = directional_positions[previous[layer]]
    r1, c1 = directional_positions[current]

    dr = abs(r1 - r0)
    dc = abs(c1 - c0)

    previous[layer] = current

    if r1 < r0:
        if c1 < c0:
            for _ in range(dc):
                total += directional_keypad("<", layer - 1)

            for _ in range(dr):
                total += directional_keypad("^", layer - 1)

        else:
            if c0 != 0:
                for _ in range(dr):
                    total += directional_keypad("^", layer - 1)

            for _ in range(dc):
                total += directional_keypad(">", layer - 1)

            if c0 == 0:
                for _ in range(dr):
                    total += directional_keypad("^", layer - 1)

    else:
        if c1 < c0:
            if c1 != 0:
                for _ in range(dc):
                    total += directional_keypad("<", layer - 1)

            for _ in range(dr):
                total += directional_keypad("v", layer - 1)

            if c1 == 0:
                for _ in range(dc):
                    total += directional_keypad("<", layer - 1)

        else:
            for _ in range(dr):
                total += directional_keypad("v", layer - 1)

            for _ in range(dc):
                total += directional_keypad(">", layer - 1)

    total += directional_keypad("A", layer - 1)
    memo[(current, layer, initial_previous)] = (total, previous[:layer + 1])
    return total

total = 0
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    s0 = line.strip()
    s1 = numeric_keypad(s0)

    length = 0
    for move in s1:
        length += directional_keypad(move, 25)

    total += int(s0[:3]) * length

print(total)

