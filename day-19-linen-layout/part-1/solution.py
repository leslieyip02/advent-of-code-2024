import sys

lines = [line.strip() for line in sys.stdin if len(line.strip()) != 0]
available = [towel.strip() for towel in lines[0].split(", ")]

ok = set()
ok.update(available)
not_ok = set()

def possible(desired):
    if desired == "" or desired in ok:
        return True
    if desired in not_ok:
        return False

    for towel in available:
        if desired.startswith(towel) and possible(desired[len(towel):]):
            ok.add(desired)
            return True

    not_ok.add(desired)
    return False

total = 0
for desired in lines[1:]:
    if possible(desired):
        total += 1

print(total)

