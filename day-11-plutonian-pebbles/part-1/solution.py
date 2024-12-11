stones = [int(i) for i in input().strip().split(" ")]

def blink(stones):
    buffer = []
    for stone in stones:
        if stone == 0:
            buffer.append(1)
        elif (l := len(str(stone))) % 2 == 0:
            mid = l // 2
            buffer.append(int(str(stone)[:mid]))
            buffer.append(int(str(stone)[mid:]))
        else:
            buffer.append(stone * 2024)
    return buffer

for _ in range(25):
    stones = blink(stones)

print(len(stones))

