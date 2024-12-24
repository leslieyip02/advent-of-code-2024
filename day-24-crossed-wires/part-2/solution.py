import sys

bits = {}
equations_by_bit = {}

lines = [line.strip() for line in sys.stdin if len(line.strip()) != 0]
for line in lines:
    if ": " in line:
        bit, value = line.split(": ")
        bits[bit] = int(value)

    else:
        a, op, b, _, c = line.split(" ")

        equations_by_bit[a] = equations_by_bit.get(a, [])
        equations_by_bit[a].append((op, b, c))
        equations_by_bit[b] = equations_by_bit.get(b, [])
        equations_by_bit[b].append((op, a, c))

        bits[c] = -1

def bits_to_int(letter, bits):
    filtered = { k: v for k, v in bits.items() if letter in k }
    values = []
    for k in sorted(filtered.keys(), reverse=True):
        values.append(str(bits[k]))

    return int("".join(values), base=2)

def apply(op, a, b, bits):
    if op == "AND":
        return bits[a] & bits[b]
    elif op == "OR":
        return bits[a] | bits[b]
    else:
        return bits[a] ^ bits[b]

def evaluate(bits, equations_by_bit):
    while len(equations_by_bit) != 0:
        for a, equations in equations_by_bit.items():
            if bits[a] != -1:
                for op, b, c in equations:
                    if bits[c] != -1:
                        continue

                    if bits[b] != -1:
                        bits[c] = apply(op, a, b, bits)

                break

        del equations_by_bit[a]

    return bits_to_int("z", bits)

# thank god for reddit
# https://www.reddit.com/r/adventofcode/comments/1hla5ql/2024_day_24_part_2_a_guide_on_the_idea_behind_the/

problem_bits_1 = []
problem_bits_2 = []
for a, equations in equations_by_bit.items():
    for i, (op, b, c) in enumerate(equations):
        if "z" in c and c != "z45":
            if op != "XOR" and c not in problem_bits_1:
                problem_bits_1.append(c)

        elif "z" not in c:
            if "x" not in a and "y" not in a and "x" not in b and "y" not in b:
                if op == "XOR" and c not in problem_bits_2:
                    problem_bits_2.append(c)

print(problem_bits_1)
print(problem_bits_2)
print()

def visit(a):
    if a not in equations_by_bit:
        return a
    return visit(equations_by_bit[a][0][2])

for bit in problem_bits_2:
    print(f"{bit} -> {visit(bit)}")
print()

for a, equations in equations_by_bit.items():
    for i, (op, b, c) in enumerate(equations):
        if c == "fhp":
            equations_by_bit[a][i] = (op, b, "z20")
        elif c == "z20":
            equations_by_bit[a][i] = (op, b, "fhp")

        elif c == "fcd":
            equations_by_bit[a][i] = (op, b, "z33")
        elif c == "z33":
            equations_by_bit[a][i] = (op, b, "fcd")

        elif c == "hmk":
            equations_by_bit[a][i] = (op, b, "z16")
        elif c == "z16":
            equations_by_bit[a][i] = (op, b, "hmk")

x0 = bits_to_int("x", bits)
y0 = bits_to_int("y", bits)
z0 = x0 + y0

z1 = evaluate({ k: v for k, v in bits.items() }, { k: [triple[::] for triple in v] for k, v in equations_by_bit.items() })
print(bin(z0)[2:].zfill(46))
print(bin(z1)[2:].zfill(46))
print(bin(z0 ^ z1)[2:].zfill(46))
print()

# mismatch starts at z27
for line in lines:
    if "x27" in line and "y27" in line:
        print(line)
print()

for a, equations in equations_by_bit.items():
    for i, (op, b, c) in enumerate(equations):
        if c == "tpc":
            equations_by_bit[a][i] = (op, b, "rvf")
        elif c == "rvf":
            equations_by_bit[a][i] = (op, b, "tpc")

z2 = evaluate({ k: v for k, v in bits.items() }, { k: [triple[::] for triple in v] for k, v in equations_by_bit.items() })
print(bin(z0)[2:].zfill(46))
print(bin(z2)[2:].zfill(46))
print(bin(z0 ^ z2)[2:].zfill(46))
print()

swapped = ["rvf", "tpc", "hmk", "fcd", "fhp", "z16", "z20", "z33"]
print(",".join(sorted(swapped)))

