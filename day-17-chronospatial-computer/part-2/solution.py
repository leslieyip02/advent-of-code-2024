a = int(input().split(": ")[1])
b = int(input().split(": ")[1])
c = int(input().split(": ")[1])

input()

program = input().split(": ")[1]
nums = [int(i) for i in program.split(",")]

def run(a):
    def combo_operand(value):
        if value <= 3:
            return value

        return [a, b, c][value - 4]

    b = 0
    c = 0

    pointer = 0
    outputs = []
    while pointer < len(nums):
        instruction = nums[pointer]
        if instruction == 0:
            a //= (1 << combo_operand(nums[pointer + 1]))
            pointer += 2

        elif instruction == 1:
            b ^= nums[pointer + 1]
            pointer += 2

        elif instruction == 2:
            b = combo_operand(nums[pointer + 1]) % 8
            pointer += 2

        elif instruction == 3:
            if a == 0:
                pointer += 2

            else:
                pointer = nums[pointer + 1]

        elif instruction == 4:
            b ^= c
            pointer += 2

        elif instruction == 5:
            outputs.append(combo_operand(nums[pointer + 1]) % 8)
            pointer += 2

        elif instruction == 6:
            b = a // (1 << combo_operand(nums[pointer + 1]))
            pointer += 2

        elif instruction == 7:
            c = a // (1 << combo_operand(nums[pointer + 1]))
            pointer += 2

        else:
            break

    return ",".join(str(i) for i in outputs), a, b, c

i = 1
j = 1

while j <= len(program):
    result, a, b, c = run(i)
    if result[-j:] == program[-j:]:
        print(i, result[-j:])

        i *= 8
        j += 2
        continue

    i += 1

