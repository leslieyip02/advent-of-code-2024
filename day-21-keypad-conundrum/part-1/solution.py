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
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
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

    return "".join(moves)

def directional_keypad(target):
    moves = []

    previous = "A"
    for current in target:
        r0, c0 = directional_positions[previous]
        r1, c1 = directional_positions[current]

        dr = abs(r1 - r0)
        dc = abs(c1 - c0)

        if r1 < r0:
            if c1 < c0:
                moves.extend(["<"] * dc)
                moves.extend(["^"] * dr)

            else:
                if c0 != 0:
                    moves.extend(["^"] * dr)
                moves.extend([">"] * dc)
                if c0 == 0:
                    moves.extend(["^"] * dr)

        else:
            if c1 < c0:
                if c1 != 0:
                    moves.extend(["<"] * dc)
                moves.extend(["v"] * dr)
                if c1 == 0:
                    moves.extend(["<"] * dc)

            else:
                moves.extend(["v"] * dr)
                moves.extend([">"] * dc)

        moves.append("A")
        previous = current

    return "".join(moves)


total = 0
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    s0 = line.strip()
    s1 = numeric_keypad(s0)
    s2 = directional_keypad(s1)
    s3 = directional_keypad(s2)

    print(s0)
    print(s1)
    print(s2)
    print(s3)
    print(int(s0[:3]), len(s3))
    total += int(s0[:3]) * len(s3)
    print()

print(total)
