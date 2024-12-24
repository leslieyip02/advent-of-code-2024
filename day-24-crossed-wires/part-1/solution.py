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

def apply(op, a, b):
    if op == "AND":
        return bits[a] & bits[b]
    elif op == "OR":
        return bits[a] | bits[b]
    else:
        return bits[a] ^ bits[b]

while len(equations_by_bit) != 0:
    for a, equations in equations_by_bit.items():
        if bits[a] != -1:
            for op, b, c in equations:
                if bits[c] != -1:
                    continue

                if bits[b] != -1:
                    bits[c] = apply(op, a, b)

            break

    del equations_by_bit[a]

z = { k: v for k, v in bits.items() if "z" in k }
values = []
for k in sorted(z.keys(), reverse=True):
    values.append(str(bits[k]))

print(int("".join(values), base=2))

