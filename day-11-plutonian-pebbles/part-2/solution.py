stones = [int(i) for i in input().strip().split(" ")]

memo = {}

def blink(stone, times):
    if times == 0:
        return 1

    if (stone, times) in memo:
        return memo[(stone, times)]

    if stone == 0:
        count = blink(1, times - 1)

    elif (l := len(str(stone))) % 2 == 0:
        mid = l // 2
        count = blink(int(str(stone)[:mid]), times - 1) + blink(int(str(stone)[mid:]), times - 1)

    else:
        count = blink(stone * 2024, times - 1)

    memo[(stone, times)] = count
    return count

total = 0
for stone in stones:
    total += blink(stone, 75)

print(total)

